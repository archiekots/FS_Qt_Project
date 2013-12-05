import pymel.core as pm

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def returnKeyedAttrs(obj):
    keys = {}
    for attr in obj.listAnimatable():
        keys.update({attr.name():chunks(pm.keyframe(attr, query=True), 3)})
    return keys