import sys
import maya

### list of Matrial Attr###
VrayAryList=[]
VraySclList=[]

AiAryList=[]
AiSclList=[]



#list selected material
list = maya.cmds.ls(sl=True)
mtGlm=list[0]
print mtGlm
#rename vray shader
mtVR=(mtGlm+"Vray")
print mtVR
maya.cmds.rename(mtGlm,mtGlm+"Vray")
#get shading group name
listSG = maya.cmds.listConnections(mtVR,d=True,type='shadingEngine')
SG = listSG[0]
print SG,mtVR
cmds.select(mtVR)

#get input of Vray Shader
if (cmds.nodeType(mtVR)=='VRayMtl'):
    #make ArnoldMaterial
    matAi = maya.cmds.shadingNode('aiStandardSurface',asShader=True)
    maya.cmds.rename(matAi,mtGlm)
    cmds.connectAttr((mtGlm+".outColor"),(SG+'.surfaceShader'),f=True)


####################
#get Vray connection
#####################
## Diffuse Amount ##
diffAmtInput = maya.cmds.listConnections((mtVR+'.diffuseColorAmount'),d=True,p=1)
if not diffAmtInput:
    diffValue= cmds.getAttr(mtVR+'.diffuseColorAmount' )
    cmds.setAttr((mtGlm+'.base'),diffValue)
else :
    cmds.connectAttr(diffInput[0],(mtGlm+'.base'),f=True)

## Diffuse Color ##
diffInput = maya.cmds.listConnections((mtVR+'.diffuseColor'),d=True,p=1)
if not diffInput:
    difValue= cmds.getAttr(mtVR+'.diffuseColor' )
    cmds.setAttr(mtGlm+'.baseColor',difValue)
else :
    cmds.connectAttr(diffInput[0],(mtGlm+'.baseColor'),f=True)

## Diffuse Roughness ##    
roughAmtInput = maya.cmds.listConnections((mtVR+'.roughnessAmount'),d=True,p=1)
if not roughAmtInput:
    roughAmtValue= cmds.getAttr(mtVR+'.roughnessAmount' )
    cmds.setAttr(mtGlm+'.diffuseRoughness',roughAmtValue)
else :
    cmds.connectAttr(diffInput[0],(mtGlm+'.diffuseRoughness'),f=True)

## Specular Amount ##
specAmtInput = maya.cmds.listConnections((mtVR+'.reflectionColorAmount'),d=True,p=1)
if not specAmtInput:
    specValue= cmds.getAttr(mtVR+'.reflectionColorAmount' )
    print specValue
    print cmds.getAttr(mtGlm+'.specular')
    cmds.setAttr((mtGlm+'.specular'),specValue)
else :
    cmds.connectAttr(specAmtInput[0],(mtGlm+'.specular'),f=True)

## Specular Color ##
specInput = maya.cmds.listConnections((mtVR+'.reflectionColor'),d=True,p=1)
if not specInput:
    specValue= cmds.getAttr(mtVR+'.reflectionColor' )
    print  cmds.getAttr(mtGlm+'.specularColor')
    cmds.setAttr((mtGlm+'.specularColorR'),specValue[0][0])
    cmds.setAttr((mtGlm+'.specularColorG'),specValue[0][1])
    cmds.setAttr((mtGlm+'.specularColorB'),specValue[0][0])
else :
    cmds.connectAttr(specInput[0],(mtGlm+'.specularColor'),f=True)

## Specular Roughness ##
specRougInput = maya.cmds.listConnections((mtVR+'.reflectionGlossiness'),d=True,p=1)
if not specRougInput:
    specValue= cmds.getAttr(mtVR+'.reflectionGlossiness' )
    cmds.setAttr(mtGlm+'.specularRoughness',(1-specValue))
else :
    invertNode = cmds.shadingNode('reverse',asUtility=True)
    cmds.connectAttr(specRougInput[0],(invertNode+'.inputX'),f=True)
    cmds.connectAttr((invertNode+'.outputX'),(mtGlm+'.specularRoughness'),f=True)
    
## Specular IOR ##
specIORInput = maya.cmds.listConnections((mtVR+'.fresnelIOR'),d=True,p=1)

if not specIORInput:
    specIORValue= cmds.getAttr(mtVR+'.fresnelIOR')
    print specIORValue
    cmds.setAttr(mtGlm+'.specularIOR',specIORValue)
else :
    cmds.connectAttr(specIORInput,(mtGlm+'.specularIOR'),f=True)



## Anisotropy and Rotation ##
Anisotropy = cmds.getAttr((mtVR+".anisotropy"))
cmds.setAttr((mtGlm+'.specularAnisotropy'),Anisotropy)
Rotation = cmds.getAttr((mtVR+".anisotropyRotation"))
cmds.setAttr((mtGlm+'.specularRotation'),Rotation)

## BumpMap ##
bumpMapInput = []
bumpMapInput = maya.cmds.listConnections((mtVR+'.bumpMap'),d=True,p=1)
 
if not bumpMapInput:
    pass
else :
    cmds.connectAttr(bumpMapInput[0],(mtGlm+'.normalCamera'),f=True)

## Bump ##
bumpOpaInput = maya.cmds.listConnections((mtVR+'.bumpMult'),d=True,p=1)
print bumpOpaInput
if not bumpOpaInput:
    bumpOpaValue= cmds.getAttr(mtVR+'.bumpMult')
    cmds.setAttr(mtGlm+'.opacityR',(bumpOpaValue))  
    cmds.setAttr(mtGlm+'.opacityG',(bumpOpaValue))  
    cmds.setAttr(mtGlm+'.opacityB',(bumpOpaValue))  
else :
    cmds.connectAttr(bumpOpaInput,(mtGlm+'.opacityR'),f=True)
    cmds.connectAttr(bumpOpaInput,(mtGlm+'.opacityG'),f=True)
    cmds.connectAttr(bumpOpaInput,(mtGlm+'.opacityB'),f=True)



