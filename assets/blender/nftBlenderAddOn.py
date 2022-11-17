#!/usr/bin/env python3

import bpy,random,copy,json,os
from bpy.props import StringProperty as StringProperty,BoolProperty,IntProperty,FloatProperty,EnumProperty,PointerProperty,CollectionProperty
from bpy.types import Panel,Operator,PropertyGroup

bl_info = {
    "name": "NFT random generator",
    "description": "Generate assets combinations",
    "author": "Doudou",
    "version": (1, 0, 0),
    "blender": (3, 3, 1),
    "category": "Scene"
}

class W(PropertyGroup):
	maxIterations:IntProperty(name=t,description='Max number',default=0,min=0)
	desiredIterations:IntProperty(name=t,description='Desired number of combinations you want to generate',default=0,min=0)
	isExportGLB:BoolProperty(name='Export to GLB files',description='Exports each combination into seperate file',default=True)
	isGeneratorRun:BoolProperty(name='Generator is running',description='',default=True)
	nameOfObjects:StringProperty(name='Name of NFTs')
	description:StringProperty(name='Description')

class X(PropertyGroup):
	rarity:IntProperty(name='Rarity',description='The higher the number the more rare it is',default=0,min=0,max=99)

class NftAddOnPanel(bpy.types.Panel):
	bl_label='Raptor Generator Free'
	bl_idname='SCENE_PT_layout'
	bl_space_type='PROPERTIES'
	bl_region_type='WINDOW'
	bl_context='scene'
	checkboxes=[True, False]
	objectIDs=[10000,8000,1000,2000,3000,7000,9000,4000,5000,6000]
	hardTree='exportOption'
	def draw(self,context):
		count=0
		attributes = list(filter(isAttributeCollection, bpy.data.collections.keys()))
		for attribute in attributes:
			self.layout.label(text=attribute)
			for attributeValue in bpy.data.collections[attribute].children.keys():
				if count<len(context.scene.traitSettings):
					attributeRow = self.layout.row()
					attributeRow.label(text='- '+attributeValue)
					attributeRow.prop(context.scene.traitSettings[count],'rarity')
					count+=1
		separatorRow = self.layout.row()
		separatorRow.separator()
		self.layout.prop(context.scene.generatorSettings,'desiredIterations')
		analyzeButtonRow = self.layout.row()
		analyzeButtonRow.scale_y=3.0
		analyzeButtonRow.operator('wm.analyze_operator')
		generateButtonRow = self.layout.row()
		generateButtonRow.scale_y=3.0
		generateButtonRow.operator('wm.hide_operator')

class AnalyzeFunction(bpy.types.Operator):
	bl_idname='wm.analyze_operator'
	bl_label='Analyze scene'
	objectIDs=[10000,8000,1000,2000,3000,7000,9000,4000,5000,6000]
	hardTree='exportOption'
	def execute(self, context):
		print('Started analazing...')
		context.scene.traitSettings.clear()
		self.filteredAttributes = list(filter(isAttributeCollection, bpy.data.collections.keys()))
		C=1;P=0
		for attribute in self.filteredAttributes:
			K=bpy.data.collections[attribute].children.keys();
			C=C*len(bpy.data.collections[attribute].children.keys())
			for attributeValue in bpy.data.collections[attribute].children.keys():
				context.scene.traitSettings.add().name=attributeValue
				context.scene.traitSettings.add().rarity=50
			P+=1
		if C==1:
			C=0
		context.scene.generatorSettings.maxIterations=C
		context.scene.generatorSettings.desiredIterations=C
		print('Analazing done!')
		return{'FINISHED'}
