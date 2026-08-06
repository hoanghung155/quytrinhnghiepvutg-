# -*- coding: utf-8 -*-
"""Thu vien sinh file BPMN 2.0 (.bpmn) kem BPMNDI, va anh xuat PNG.

Dung chung cho ba mo hinh cua Danh: M2, C3, C4.
File .bpmn mo duoc bang bpmn.io, Camunda Modeler, Signavio.
"""
from xml.sax.saxutils import escape

NS = ('xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
      'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
      'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
      'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
      'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
      'targetNamespace="http://uit.edu.vn/bpm/tgdd"')

SIZE = {"start": (36, 36), "end": (36, 36), "task": (150, 80),
        "gw": (50, 50), "inter": (36, 36)}
TAG = {"start": "startEvent", "end": "endEvent", "task": "task",
       "gw": "exclusiveGateway", "inter": "intermediateCatchEvent"}

COL_W, LANE_H, ROW_H, X0, Y0 = 200, 220, 100, 160, 80


class Proc:
    def __init__(self, pid, name, lanes):
        self.pid, self.name = pid, name
        self.lanes = lanes                 # list ten lane, theo thu tu tu tren xuong
        self.el = {}                       # eid -> dict
        self.fl = []                       # (fid, src, dst, name)
        self._n = 0

    def add(self, kind, eid, name, lane, col, row=0, gwtype="exclusive"):
        w, h = SIZE[kind]
        li = self.lanes.index(lane)
        cxp = X0 + col * COL_W
        cyp = Y0 + li * LANE_H + 60 + row * ROW_H
        self.el[eid] = dict(kind=kind, name=name, lane=lane, li=li, col=col, row=row,
                            x=cxp, y=cyp, w=w, h=h, gwtype=gwtype)
        return eid

    def flow(self, src, dst, name=""):
        self._n += 1
        self.fl.append(("f%d" % self._n, src, dst, name))

    # ---- hinh hoc ------------------------------------------------------
    def _c(self, eid):
        e = self.el[eid]
        return e["x"] + e["w"] / 2, e["y"] + e["h"] / 2

    def _wp(self, src, dst):
        """Waypoint don gian: ra canh phai nguon, vao canh trai dich, be goc neu lech hang."""
        a, b = self.el[src], self.el[dst]
        ay, by = a["y"] + a["h"] / 2, b["y"] + b["h"] / 2
        if b["x"] >= a["x"] + a["w"]:
            p1 = (a["x"] + a["w"], ay)
            p2 = (b["x"], by)
            if abs(ay - by) < 2:
                return [p1, p2]
            mx = (p1[0] + p2[0]) / 2
            return [p1, (mx, ay), (mx, by), p2]
        # di lui hoac cung cot -> vong duoi
        p1 = (a["x"] + a["w"] / 2, a["y"] + a["h"])
        p2 = (b["x"] + b["w"] / 2, b["y"] + b["h"])
        low = max(p1[1], p2[1]) + 45
        return [p1, (p1[0], low), (p2[0], low), p2]

    def bounds(self):
        xs = [e["x"] + e["w"] for e in self.el.values()]
        ys = [e["y"] + e["h"] for e in self.el.values()]
        return max(xs) + 120, max(ys) + 90

    # ---- xuat XML ------------------------------------------------------
    def to_bpmn(self):
        W, H = self.bounds()
        o = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<bpmn:definitions %s id="Defs_%s">' % (NS, self.pid),
             '  <bpmn:collaboration id="Collab_%s">' % self.pid,
             '    <bpmn:participant id="Part_%s" name="%s" processRef="%s"/>'
             % (self.pid, escape(self.name), self.pid),
             '  </bpmn:collaboration>',
             '  <bpmn:process id="%s" name="%s" isExecutable="false">'
             % (self.pid, escape(self.name)),
             '    <bpmn:laneSet id="LaneSet_%s">' % self.pid]
        for i, ln in enumerate(self.lanes):
            o.append('      <bpmn:lane id="Lane_%d" name="%s">' % (i, escape(ln)))
            for eid, e in self.el.items():
                if e["lane"] == ln:
                    o.append('        <bpmn:flowNodeRef>%s</bpmn:flowNodeRef>' % eid)
            o.append('      </bpmn:lane>')
        o.append('    </bpmn:laneSet>')

        for eid, e in self.el.items():
            tag = TAG[e["kind"]]
            if e["kind"] == "gw" and e["gwtype"] == "parallel":
                tag = "parallelGateway"
            ins = [f[0] for f in self.fl if f[2] == eid]
            outs = [f[0] for f in self.fl if f[1] == eid]
            o.append('    <bpmn:%s id="%s" name="%s">' % (tag, eid, escape(e["name"])))
            for f in ins:
                o.append('      <bpmn:incoming>%s</bpmn:incoming>' % f)
            for f in outs:
                o.append('      <bpmn:outgoing>%s</bpmn:outgoing>' % f)
            o.append('    </bpmn:%s>' % tag)
        for fid, s, d, nm in self.fl:
            o.append('    <bpmn:sequenceFlow id="%s" name="%s" sourceRef="%s" targetRef="%s"/>'
                     % (fid, escape(nm), s, d))
        o.append('  </bpmn:process>')

        # --- BPMNDI ---
        o += ['  <bpmndi:BPMNDiagram id="Diag_%s">' % self.pid,
              '    <bpmndi:BPMNPlane id="Plane_%s" bpmnElement="Collab_%s">'
              % (self.pid, self.pid),
              '      <bpmndi:BPMNShape id="Sh_Part_%s" bpmnElement="Part_%s" isHorizontal="true">'
              % (self.pid, self.pid),
              '        <dc:Bounds x="60" y="%d" width="%d" height="%d"/>'
              % (Y0, W - 100, len(self.lanes) * LANE_H),
              '      </bpmndi:BPMNShape>']
        for i, ln in enumerate(self.lanes):
            o += ['      <bpmndi:BPMNShape id="Sh_Lane_%d" bpmnElement="Lane_%d" isHorizontal="true">'
                  % (i, i),
                  '        <dc:Bounds x="90" y="%d" width="%d" height="%d"/>'
                  % (Y0 + i * LANE_H, W - 130, LANE_H),
                  '      </bpmndi:BPMNShape>']
        for eid, e in self.el.items():
            o += ['      <bpmndi:BPMNShape id="Sh_%s" bpmnElement="%s">' % (eid, eid),
                  '        <dc:Bounds x="%d" y="%d" width="%d" height="%d"/>'
                  % (e["x"], e["y"], e["w"], e["h"]),
                  '      </bpmndi:BPMNShape>']
        for fid, s, d, nm in self.fl:
            o.append('      <bpmndi:BPMNEdge id="Ed_%s" bpmnElement="%s">' % (fid, fid))
            for p in self._wp(s, d):
                o.append('        <di:waypoint x="%d" y="%d"/>' % (round(p[0]), round(p[1])))
            o.append('      </bpmndi:BPMNEdge>')
        o += ['    </bpmndi:BPMNPlane>', '  </bpmndi:BPMNDiagram>', '</bpmn:definitions>', '']
        return "\n".join(o)

    def n_gateway(self):
        return sum(1 for e in self.el.values() if e["kind"] == "gw")


# ====================== xuat anh PNG ======================================
def _font(size, bold=False):
    from PIL import ImageFont
    for p in ("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
              "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


def _wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textbbox((0, 0), t, font=font)[2] <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render_png(proc, path, title):
    from PIL import Image, ImageDraw
    import math
    W, H = proc.bounds()
    W, H = int(W), int(H + 70)
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    F_T, F_L, F_E, F_F = _font(24, True), _font(16, True), _font(14), _font(12)
    BK, GR = (25, 25, 25), (120, 120, 120)
    LANE_FILL = [(238, 244, 255), (255, 248, 232), (238, 250, 240), (250, 240, 248)]

    d.text((60, 20), title, font=F_T, fill=BK)
    for i, ln in enumerate(proc.lanes):
        y = Y0 + i * LANE_H + 50
        d.rectangle([60, y, W - 40, y + LANE_H], fill=LANE_FILL[i % 4], outline=(170, 170, 170))
        d.rectangle([60, y, 150, y + LANE_H], fill=(245, 245, 245), outline=(170, 170, 170))
        for j, part in enumerate(_wrap(d, ln, F_L, LANE_H - 20)):
            d.text((72, y + 14 + j * 20), part, font=F_L, fill=(60, 60, 60))

    for fid, s, t, nm in proc.fl:
        pts = [(p[0], p[1] + 50) for p in proc._wp(s, t)]
        d.line(pts, fill=(90, 90, 90), width=2)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        a = math.atan2(y2 - y1, x2 - x1)
        for sgn in (2.6, -2.6):
            d.line([(x2, y2), (x2 + 12 * math.cos(a + sgn), y2 + 12 * math.sin(a + sgn))],
                   fill=(90, 90, 90), width=2)
        if nm:
            mid = pts[len(pts) // 2]
            bb = d.textbbox((0, 0), nm, font=F_F)
            tx, ty = mid[0] - (bb[2] - bb[0]) / 2, mid[1] - 17
            d.rectangle([tx - 3, ty - 1, tx + (bb[2] - bb[0]) + 3, ty + 14], fill=(255, 255, 255))
            d.text((tx, ty), nm, font=F_F, fill=(150, 60, 60))

    for eid, e in proc.el.items():
        x, y, w, h = e["x"], e["y"] + 50, e["w"], e["h"]
        k = e["kind"]
        if k in ("start", "end", "inter"):
            wd = 4 if k == "end" else 2
            d.ellipse([x, y, x + w, y + h], fill=(255, 255, 255),
                      outline=(60, 140, 60) if k == "start" else (170, 50, 50), width=wd)
            for j, ln in enumerate(_wrap(d, e["name"].replace("\n", " "), F_F, 150)):
                bb = d.textbbox((0, 0), ln, font=F_F)
                d.text((x + w / 2 - (bb[2] - bb[0]) / 2, y + h + 4 + j * 14), ln,
                       font=F_F, fill=BK)
        elif k == "gw":
            cx, cy, r = x + w / 2, y + h / 2, w / 2
            d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)],
                      fill=(255, 252, 225), outline=(200, 160, 40), width=2)
            d.text((cx - 6, cy - 9), "+" if e["gwtype"] == "parallel" else "X", font=F_L, fill=BK)
            gl = _wrap(d, e["name"], F_F, 165)
            for j, ln in enumerate(gl):
                bb = d.textbbox((0, 0), ln, font=F_F)
                d.text((cx - (bb[2] - bb[0]) / 2, y - 6 - (len(gl) - j) * 14), ln,
                       font=F_F, fill=(120, 80, 10))
        else:
            d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=(255, 255, 255),
                                outline=(70, 110, 180), width=2)
            lines = _wrap(d, e["name"], F_E, w - 16)
            for j, ln in enumerate(lines):
                bb = d.textbbox((0, 0), ln, font=F_E)
                d.text((x + w / 2 - (bb[2] - bb[0]) / 2,
                        y + h / 2 - len(lines) * 9 + j * 18), ln, font=F_E, fill=BK)

    d.text((60, H - 26), "Nguồn: nhóm tự lập — %d gateway." % proc.n_gateway(),
           font=F_F, fill=GR)
    img.save(path)
    return img.size
