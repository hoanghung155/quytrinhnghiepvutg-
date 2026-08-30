# -*- coding: utf-8 -*-
"""Dem gateway va kiem tra BPMNDI tren chinh file .bpmn.

Doc file XML da sinh ra, KHONG doc script sinh — de con so bao cao la con so
that su nam trong file ma bpmn.io / Camunda Modeler se mo.

Chay: python model/bpmn/dem_gateway.py
Tren Windows neu console bao loi ma hoa thi dat PYTHONIOENCODING=utf-8.

Kiem tra bon thu voi moi file:
  1. XML hop le, parse duoc.
  2. Dem gateway theo tung loai — yeu cau do phuc tap la HON 7.
  3. Moi flow node co mot BPMNShape trong phan BPMNDI.
  4. Moi sequenceFlow co mot BPMNEdge voi it nhat 2 waypoint.

Thieu BPMNDI thi file van hop le ve mat XML nhung mo ra se khong thay hinh —
day la loi hay gap nhat khi sinh .bpmn bang script.
"""
import sys
import pathlib
import xml.etree.ElementTree as ET

D = pathlib.Path(__file__).resolve().parent

BPMN = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
DI = "{http://www.omg.org/spec/BPMN/20100524/DI}"
DIW = "{http://www.omg.org/spec/DD/20100524/DI}"

NGUONG_GATEWAY = 7  # yeu cau: HON 7

LOAI_GATEWAY = [
    "exclusiveGateway",
    "parallelGateway",
    "inclusiveGateway",
    "eventBasedGateway",
    "complexGateway",
]

# Cac the duoc coi la flow node (phai co BPMNShape).
FLOW_NODE = LOAI_GATEWAY + [
    "task", "userTask", "serviceTask", "manualTask", "sendTask", "receiveTask",
    "scriptTask", "businessRuleTask", "subProcess", "callActivity",
    "startEvent", "endEvent", "intermediateCatchEvent", "intermediateThrowEvent",
    "boundaryEvent",
]


def kiem_tra(path):
    ten = path.name
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        print("%-34s XML LOI: %s" % (ten, e))
        return False

    # --- dem gateway theo loai ---
    dem = {}
    for loai in LOAI_GATEWAY:
        n = len(root.findall(".//%s%s" % (BPMN, loai)))
        if n:
            dem[loai] = n
    tong_gw = sum(dem.values())

    # --- thu thap flow node va sequence flow ---
    nodes = []
    for loai in FLOW_NODE:
        nodes += [e.get("id") for e in root.findall(".//%s%s" % (BPMN, loai))]
    flows = [e.get("id") for e in root.findall(".//%ssequenceFlow" % BPMN)]

    # --- thu thap BPMNDI ---
    shapes = {e.get("bpmnElement") for e in root.findall(".//%sBPMNShape" % DI)}
    edges = {}
    for e in root.findall(".//%sBPMNEdge" % DI):
        edges[e.get("bpmnElement")] = len(e.findall("%swaypoint" % DIW))

    thieu_shape = [n for n in nodes if n not in shapes]
    thieu_edge = [f for f in flows if f not in edges]
    edge_kem = [f for f, n in edges.items() if n < 2]

    gw_dat = tong_gw > NGUONG_GATEWAY
    di_dat = not thieu_shape and not thieu_edge and not edge_kem

    chi_tiet = ", ".join("%s=%d" % (k.replace("Gateway", ""), v) for k, v in dem.items())
    print("%-34s gateway: %2d (%s) | node: %2d | flow: %2d | BPMNDI: %s%s"
          % (ten, tong_gw, chi_tiet or "khong co", len(nodes), len(flows),
             "du" if di_dat else "THIEU",
             "" if gw_dat else "  <-- CHUA HON %d" % NGUONG_GATEWAY))

    if thieu_shape:
        print("    thieu BPMNShape cho %d node: %s" % (len(thieu_shape), thieu_shape[:5]))
    if thieu_edge:
        print("    thieu BPMNEdge cho %d flow: %s" % (len(thieu_edge), thieu_edge[:5]))
    if edge_kem:
        print("    BPMNEdge duoi 2 waypoint: %s" % edge_kem[:5])

    return gw_dat and di_dat


def main():
    files = sorted(D.glob("*.bpmn"))
    if not files:
        print("Khong tim thay file .bpmn nao trong %s" % D)
        return 1
    print("Nguong do phuc tap: HON %d gateway\n" % NGUONG_GATEWAY)
    ket_qua = [kiem_tra(f) for f in files]
    hong = ket_qua.count(False)
    print()
    print("Ket qua: %d/%d file dat" % (len(ket_qua) - hong, len(ket_qua)))
    return 1 if hong else 0


if __name__ == "__main__":
    sys.exit(main())
