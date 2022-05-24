import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("Z:/git/ML_WPT_coil/LRT/simple_model/script1/ML_aedt/ML1.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML1")
oProject.InsertDesign("Maxwell", "Maxwell_ML_v$VERSION_IDX_STR", "EddyCurrent", "")
oDesign = oProject.SetActiveDesign("Maxwell_ML_v$VERSION_IDX_STR")

# Make setup
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("EddyCurrent", 
	[
		"NAME:Setup1",
		"EnableZ:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"MaximumPasses:="	, 5,
		"MinimumPasses:="	, 5,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"SolveFieldOnly:="	, False,
		"PercentError:="	, 1E-12,
		"SolveMatrixAtLast:="	, True,
		"PercentError:="	, 1E-12,
		"CacheSaveKinZ:="	, "Delta",
		"ConstantDelta:="	, "0s",
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-05,
		"NonLinearResidual:="	, 0.0001,
		"SmoothBHCurve:="	, False,
		"Frequency:="		, "60e+3Hz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunZ:=", False,
		"UseMuLink:="		, False
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
					"NAME:air_gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "200mm"
					
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
					"NAME:move",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$movemm"
					
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
					"Value:="		, "[$width0, $width1] mm"
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
					"NAME:height",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$height0, $height1] mm"
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
					"NAME:gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$gap0, $gap1] mm"
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
					"Value:="		, "[$coil0_width, $coil0_width] mm"
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
					"NAME:ferrite_tick",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[10, 10] mm"
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
					"NAME:ferrite_x",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[1.2, 1.2]"
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
					"NAME:ferrite_y",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[1.05, 1.05]"
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
					"NAME:ter",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.2*height[0]"
					
				]
			]
		]
	])



# Make air
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-width[0]/2-ter",
		"YPosition:="		, "-height[0]/2-ter",
		"ZPosition:="		, "-150mm-air_gap/2",
		"XSize:="		, "width[0]+2*ter",
		"YSize:="		, "height[0]+2*ter",
		"ZSize:="		, "300mm+air_gap"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Air",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 1,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


# Make core

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-width[0]/2*ferrite_x[0]",
		"YPosition:="		, "-height[0]/2*ferrite_y[0]",
		"ZPosition:="		, "-air_gap/2-coil_height[0]/2",
		"XSize:="		, "width[0]*ferrite_x[0]",
		"YSize:="		, "height[0]*ferrite_y[0]",
		"ZSize:="		, "ferrite_tick[0]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_tx",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
		"XPosition:="		, "-width[1]/2*ferrite_x[1]",
		"YPosition:="		, "-height[1]/2*ferrite_y[1]-height[1]/2-move",
		"ZPosition:="		, "air_gap/2+coil_height[1]/2",
		"XSize:="		, "width[1]*ferrite_x[1]",
		"YSize:="		, "height[1]*ferrite_y[1]",
		"ZSize:="		, "ferrite_tick[1]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_rx1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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
		"XPosition:="		, "-width[1]/2*ferrite_x[1]",
		"YPosition:="		, "-height[1]/2*ferrite_y[1]+height[1]/2+move",
		"ZPosition:="		, "air_gap/2+coil_height[1]/2",
		"XSize:="		, "width[1]*ferrite_x[1]",
		"YSize:="		, "height[1]*ferrite_y[1]",
		"ZSize:="		, "ferrite_tick[1]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_rx2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
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

