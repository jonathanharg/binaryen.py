from binaryen import Module, Feature


myModule = Module()
print(myModule.get_features())
myModule.set_feature(Feature.GC | Feature.ReferenceTypes)
print(myModule.get_features())
print(list(myModule.get_features()))