from binaryen import Feature, Module

mod = Module()
print(mod.get_features())

mod.set_feature(Feature.GC | Feature.ReferenceTypes)

print(mod.get_features())
print(list(mod.get_features()))
