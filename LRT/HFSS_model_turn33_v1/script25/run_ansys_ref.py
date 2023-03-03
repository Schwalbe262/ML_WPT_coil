import ScriptEnv
import csv
import math

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("Y:/git/ML_WPT_coil/LRT/HFSS_model_turn33_v1/script25/ML_aedt/ML25.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML25")
oProject.InsertDesign("HFSS", "HFSS_ML_v$VERSION_IDX_STR", "DrivenTerminal", "") # check "HFSS_ML_v$VERSION_IDX_STR"
oDesign = oProject.SetActiveDesign("HFSS_ML_v$VERSION_IDX_STR") # check "HFSS_ML_v$VERSION_IDX_STR"

# Make setup
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "60kHz",
		"MaxDeltaE:="		, 0.001,
		"MaximumPasses:="	, 6, # check 6
		"MinimumPasses:="	, 6, # check 6
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 0,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.1,
		"UseMaxTetIncrease:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])


# Set variable

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Num",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "6"
					
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:air_gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$air_gapmm" # check $airgapmm
					
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:coil_width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$coil_width0, $coil_width1] mm" # check [$coil_width0, $coil_width1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:length",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$length0, $length1] mm" # check [$length0, $length1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$width0, $width1] mm" # check [$width0, $width1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:coil_offset",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$coil_offset0, $coil_offset1] mm" # check [$coil_offset0, $coil_offset1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:turn_length_gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$turn_length_gap0, $turn_length_gap1] mm" # check [$turn_length_gap0, $turn_length_gap1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:turn_width_gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$turn_width_gap0, $turn_width_gap1] mm" # check [$turn_width_gap0, $turn_width_gap1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ferrite_thick",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$ferrite_thick0, $ferrite_thick1] mm" # check [$ferrite_thick0, $ferrite_thick1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ferrite_length_margin",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$ferrite_length_margin0, $ferrite_length_margin1] mm" # check [$ferrite_length_margin0, $ferrite_length_margin1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ferrite_width_margin",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$ferrite_width_margin0, $ferrite_width_margin1] mm" # check [$ferrite_width_margin0, $ferrite_width_margin1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ferrite_side_height",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$ferrite_side_height0, $ferrite_side_height1] mm" # check [$ferrite_side_height0, $ferrite_side_height1] mm
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ferrite_side_thick",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$ferrite_side_thick0, $ferrite_side_thick1] mm" # check [$ferrite_side_thick0, $ferrite_side_thick1] mm
				]
			]
		]
	])



# =============================
# Make geometry
# =============================

# Make Tx core
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "- (width[0] + coil_width[0] + 2*ferrite_width_margin[0] + 2*ferrite_side_thick[0])/2",
		"YPosition:="		, "- (length[0] + coil_width[0] + 2*ferrite_length_margin[0] + 2*ferrite_side_thick[0])/2",
		"ZPosition:="		, "-air_gap/2",
		"XSize:="		, "(width[0] + coil_width[0] + 2*ferrite_width_margin[0] + 2*ferrite_side_thick[0])",
		"YSize:="		, "(length[0] + coil_width[0] + 2*ferrite_length_margin[0] + 2*ferrite_side_thick[0])",
		"ZSize:="		, "-(ferrite_side_height[0] + ferrite_thick[0])"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_tx",
		"Flags:="		, "",
		"Color:="		, "(70 70 70)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "- (width[0] + coil_width[0] + 2*ferrite_width_margin[0])/2",
		"YPosition:="		, "- (length[0] + coil_width[0] + 2*ferrite_length_margin[0])/2",
		"ZPosition:="		, "-air_gap/2",
		"XSize:="		, "(width[0] + coil_width[0] + 2*ferrite_width_margin[0])",
		"YSize:="		, "(length[0] + coil_width[0] + 2*ferrite_length_margin[0]) + ferrite_side_thick[0]",
		"ZSize:="		, "-(ferrite_side_height[0])"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_tx_sub",
		"Flags:="		, "",
		"Color:="		, "(70 70 70)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "ferrite_tx",
		"Tool Parts:="		, "ferrite_tx_sub"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])



# Make Rx core
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "- (width[1] + coil_width[1] + 2*ferrite_width_margin[1] + 2*ferrite_side_thick[1])/2",
		"YPosition:="		, "- (length[1] + coil_width[1] + 2*ferrite_length_margin[1] + 2*ferrite_side_thick[1])/2",
		"ZPosition:="		, "air_gap/2",
		"XSize:="		, "(width[1] + coil_width[1] + 2*ferrite_width_margin[1] + 2*ferrite_side_thick[1])",
		"YSize:="		, "(length[1] + coil_width[1] + 2*ferrite_length_margin[1] + 2*ferrite_side_thick[1])",
		"ZSize:="		, "(ferrite_side_height[1] + ferrite_thick[1])"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_rx",
		"Flags:="		, "",
		"Color:="		, "(70 70 70)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "(width[1] + coil_width[1] + 2*ferrite_width_margin[1])/2",
		"YPosition:="		, "(length[1] + coil_width[1] + 2*ferrite_length_margin[1])/2",
		"ZPosition:="		, "air_gap/2",
		"XSize:="		, "-(width[1] + coil_width[1] + 2*ferrite_width_margin[1])",
		"YSize:="		, "-(length[1] + coil_width[1] + 2*ferrite_length_margin[1]) - ferrite_side_thick[1]",
		"ZSize:="		, "(ferrite_side_height[1])"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_rx_sub",
		"Flags:="		, "",
		"Color:="		, "(70 70 70)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "ferrite_rx",
		"Tool Parts:="		, "ferrite_rx_sub"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])




# =================================================================================================
# Make Tx
# =================================================================================================

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]",
				"Y:="			, "1.5*(length[0])/2",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]",
				"Y:="			, "-(length[0])/2",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[0]",
				"Y:="			, "-(length[0])/2",
				"Z:="			, "0mm"
			],
            [ # point 4
				"NAME:PLPoint",
				"X:="			, "1/2*width[0]",
				"Y:="			, "(length[0])/2",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 1*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "(length[0])/2",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 1*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "-(length[0])/2 + 1*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[0] - 1*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "-(length[0])/2 + 1*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [ # point 8
				"NAME:PLPoint",
				"X:="			, "1/2*width[0] - 1*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "(length[0])/2 - 1*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 2*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "(length[0])/2 - 1*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 2*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "-(length[0])/2 + 2*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[0] - 2*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "-(length[0])/2 + 2*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [ # point 12
				"NAME:PLPoint",
				"X:="			, "1/2*width[0] - 2*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "(length[0])/2 - 2*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 3*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "(length[0])/2 - 2*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 3*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "(length[0])/2 - 2*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "1.5*coil_width[0]"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 3*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "(length[0])/2 + 1*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "1.5*coil_width[0]"
			],
            [ # point 16
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 3*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "(length[0])/2 + 1*(coil_width[0]+turn_length_gap[0])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0] + 3*(coil_width[0]+turn_width_gap[0])",
				"Y:="			, "1.5*(length[0])/2",
				"Z:="			, "0mm"
			],
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 4,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 6,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 7,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 8,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 9,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 10,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 11,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 12,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 13,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 14,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 15,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionlength:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_coil",
		"Flags:="		, "",
		"Color:="		, "(255 0 0)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, False,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_coil",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "-air_gap/2 - ferrite_side_height[0] + coil_width[0]/2 + coil_offset[0]"
	])




# =================================================================================================
# Make Rx
# =================================================================================================

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "1/2*width[1]",
				"Y:="			, "-1.5*(length[1])/2",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1]",
				"Y:="			, "(length[1])/2",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[1]",
				"Y:="			, "(length[1])/2",
				"Z:="			, "0mm"
			],
            [ # point 4
				"NAME:PLPoint",
				"X:="			, "-1/2*width[1]",
				"Y:="			, "-(length[1])/2",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 1*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-(length[1])/2",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 1*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "(length[1])/2 - 1*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[1] + 1*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "(length[1])/2 - 1*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [ # point 8
				"NAME:PLPoint",
				"X:="			, "-1/2*width[1] + 1*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-(length[1])/2 + 1*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 2*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-(length[1])/2 + 1*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 2*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "(length[1])/2 - 2*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "-1/2*width[1] + 2*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "(length[1])/2 - 2*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [ # point 12
				"NAME:PLPoint",
				"X:="			, "-1/2*width[1] + 2*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-(length[1])/2 + 2*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 3*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-(length[1])/2 + 2*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 3*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-(length[1])/2 + 2*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "-1.5*coil_width[1]"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 3*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-(length[1])/2 - 1*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "-1.5*coil_width[1]"
			],
            [ # point 16
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 3*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-(length[1])/2 - 1*(coil_width[1]+turn_length_gap[1])",
				"Z:="			, "0mm"
			],
            [
				"NAME:PLPoint",
				"X:="			, "1/2*width[1] - 3*(coil_width[1]+turn_width_gap[1])",
				"Y:="			, "-1.5*(length[1])/2",
				"Z:="			, "0mm"
			],
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 4,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 6,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 7,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 8,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 9,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 10,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 11,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 12,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 13,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 14,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 15,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionlength:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_coil",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, False,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx_coil",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "air_gap/2 + ferrite_side_height[1] - coil_width[1]/2 - coil_offset[1]"
	])



# Make Terminal

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateObjectFromEdges(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_coil",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:BodyFromEdgeToParameters",
			"Edges:="		, [283,455] # 283,455
		]
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor.Connect(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_coil_ObjectFromEdge1,Tx_coil_ObjectFromEdge2"
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		975 # 975
	], False, 
	[
		"NAME:ReferenceConductors", 
		"Tx_coil"
	], "1", True)
oModule.AssignTerminal(
	[
		"NAME:Ter_Tx",
		"Edges:="		, [978],
		"ParentBndID:="		, "1",
		"TerminalResistance:="	, "50ohm"
	])
oEditor.CreateObjectFromEdges(
	[
		"NAME:Selections",
		"Selections:="		, "Rx_coil",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:BodyFromEdgeToParameters",
			"Edges:="		, [671,852]
		]
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor.Connect(
	[
		"NAME:Selections",
		"Selections:="		, "Rx_coil_ObjectFromEdge1,Rx_coil_ObjectFromEdge2"
	])
oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		996
	], False, 
	[
		"NAME:ReferenceConductors", 
		"Rx_coil"
	], "2", True)
oModule.AssignTerminal(
	[
		"NAME:Ter_Rx",
		"Edges:="		, [999],
		"ParentBndID:="		, "2",
		"TerminalResistance:="	, "50ohm"
	])
oEditor.CreateRegion(
	[
		"NAME:RegionParameters",
		"+XPaddingType:="	, "Percentage Offset",
		"+XPadding:="		, "100",
		"-XPaddingType:="	, "Percentage Offset",
		"-XPadding:="		, "100",
		"+YPaddingType:="	, "Percentage Offset",
		"+YPadding:="		, "60",
		"-YPaddingType:="	, "Percentage Offset",
		"-YPadding:="		, "60",
		"+ZPaddingType:="	, "Percentage Offset",
		"+ZPadding:="		, "200",
		"-ZPaddingType:="	, "Percentage Offset",
		"-ZPadding:="		, "200"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Region",
		"Flags:="		, "Wireframe#",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["Region"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])
oModule = oDesign.GetModule("MeshSetup")
oModule.AssignLengthOp(
	[
		"NAME:coil",
		"RefineInside:="	, False,
		"Enabled:="		, True,
		"Objects:="		, ["Rx_coil","Tx_coil"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "100mm"
	])
oModule.AssignLengthOp(
	[
		"NAME:ferrite",
		"RefineInside:="	, False,
		"Enabled:="		, True,
		"Objects:="		, ["ferrite_rx","ferrite_tx"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "100mm"
	])
oProject.Save()
oDesign.Analyze("Setup1")


oModule = oDesign.GetModule("OutputVariable")
oModule.CreateOutputVariable("Ltx", "im(Zt(Ter_Tx,Ter_Tx))/2/pi/freq * 1e+6", "Setup1 : LastAdaptive", "Terminal Solution Data", [])
oModule.CreateOutputVariable("Lrx", "im(Zt(Ter_Rx,Ter_Rx))/2/pi/freq * 1e+6", "Setup1 : LastAdaptive", "Terminal Solution Data", [])
oModule.CreateOutputVariable("k", "im(Zt(Ter_Tx,Ter_Rx))/sqrt(im(Zt(Ter_Rx,Ter_Rx))*im(Zt(Ter_Tx,Ter_Tx)))", "Setup1 : LastAdaptive", "Terminal Solution Data", [])
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Output Variables Table 1", "Terminal Solution Data", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Num:="			, ["Nominal"],
		"air_gap:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Ltx","Lrx","k"]
	])

oModule.ExportToFile("Output Variables Table 1", "Y:/git/ML_WPT_coil/LRT/HFSS_model_turn33_v1/script25/ML_data/inductance$VERSION_IDX_STR_dat.csv", False)


results = []
with open("./ML_data/inductance$VERSION_IDX_STR_dat.csv") as csvfile:
	reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
	for row in reader: # each row is a list
		results.append(row)

Ltx = results[1][1]
Lrx = results[1][2]

V1 = Ltx * 1e-6 * 2 * 3.141592 * 60e+3 * $Itx * math.sqrt(2) 
# V1 = V1 + str("V")

V2 = Lrx * 1e-6 * 2 * 3.141592 * 60e+3 * $Irx * math.sqrt(2) 
# V2 = V2 + str("V")


oModule = oDesign.GetModule("Solutions")
oModule.EditSources(
	[
		[
			"UseIncidentVoltage:="	, False,
			"IncludePortPostProcessing:=", False,
			"SpecifySystemPower:="	, False
		],
		[
			"Name:="		, "Ter_Tx",
			"Terminated:="		, False,
			"Magnitude:="		, V1,
			"Phase:="		, "0deg"
		],
		[
			"Name:="		, "Ter_Rx",
			"Terminated:="		, False,
			"Magnitude:="		, V2,
			"Phase:="		, "90deg"
		]
	])

oModule = oDesign.GetModule("FieldsReporter")
oModule.CopyNamedExprToStack("Surface_Loss_Density")
oModule.EnterSurf("Tx_coil")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Tx_loss", "Fields")
oModule.CopyNamedExprToStack("Surface_Loss_Density")
oModule.EnterSurf("Rx_coil")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Rx_loss", "Fields")


oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Calculator Expressions Table 1", "Fields", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"Num:="			, ["Nominal"],
		"air_gap:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Tx_loss","Rx_loss"]
	])


oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Calculator Expressions Table 1", "Y:/git/ML_WPT_coil/LRT/HFSS_model_turn33_v1/script25/ML_data/loss$VERSION_IDX_STR_dat.csv", False)
