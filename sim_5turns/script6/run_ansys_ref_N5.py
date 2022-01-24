import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

address1 = "Z:\\git\\ML_WPT_coil\\script6"
address2 = "Z:\ML_WPT\ML_WPT_coil\script6"


# Open aedt file
oDesktop.OpenProject("./ML_aedt/ML6.aedt")


# Make project
oProject = oDesktop.SetActiveProject("ML6")
oProject.InsertDesign("HFSS", "HFSS_ML_v$VERSION_IDX_STR", "DrivenTerminal", "")
oDesign = oProject.SetActiveDesign("HFSS_ML_v$VERSION_IDX_STR")


# Make setup
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "$freqkHz",
		"MaxDeltaE:="		, 1e-12,
		"MaximumPasses:="	, 15,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N1"
					
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
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$w1mm"
					
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
					"NAME:w2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$w2mm"
					
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
					"NAME:w3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$w3mm"
					
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
					"NAME:w4",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$w4mm"
					
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
					"NAME:w5",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$w5mm"
					
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
					"Value:="		, "w1"
					
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
					"NAME:spacex",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$spacexmm"
					
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
					"NAME:spacey",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$spaceymm"
					
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
					"NAME:ratiox1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratiox1"
					
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
					"NAME:ratiox2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratiox2"
					
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
					"NAME:ratiox3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratiox3"
					
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
					"NAME:ratiox4",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratiox4"
					
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
					"NAME:ratiox5",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratiox5"
					
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
					"NAME:ratiox6",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratiox6"
					
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
					"NAME:ratioy1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratioy1"
					
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
					"NAME:ratioy2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratioy2"
					
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
					"NAME:ratioy3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratioy3"
					
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
					"NAME:ratioy4",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratioy4"
					
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
					"NAME:ratioy5",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$ratioy5"
					
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
					"NAME:airx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "spacex*ratiox6*2.5"
					
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
					"NAME:airy",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "spacey*ratioy5*3"
					
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
					"NAME:airz",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "50mm"
					
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
					"Value:="		, "$heightum"
					
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
					"NAME:magx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "spacex*ratiox5"
					
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
					"NAME:magy",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "spacey*ratioy5"
					
				]
			]
		]
	])


# Make air

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-airx/2",
		"YPosition:="		, "-airy/2",
		"ZPosition:="		, "-airz/2",
		"XSize:="		, "airx",
		"YSize:="		, "airy",
		"ZSize:="		, "airz"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "air",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["air"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])



# Make model

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "spacex*ratiox1-width/2",
		"YPosition:="		, "0mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "width",
		"YSize:="		, "width",
		"ZSize:="		, "-2mm-height/2"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

# Make Ter1

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox1",
				"Y:="			, "0mm",
				"Z:="			, "-2mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox1",
				"Y:="			, "-spacey*ratioy5-width*2",
				"Z:="			, "-2mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Ter1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Ter1:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "width"
				],
				[
					"NAME:Height",
					"Value:="		, "height"
				]
			]
		]
	])

# Make Ter2

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox5",
				"Y:="			, "-spacey*ratioy5",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox6",
				"Y:="			, "-spacey*ratioy5",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox6",
				"Y:="			, "-spacey*ratioy5-width*2",
				"Z:="			, "0mm"
			]
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Ter2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Ter2:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "w5"
				],
				[
					"NAME:Height",
					"Value:="		, "height"
				]
			]
		]
	])



# Make turn1

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox1",
				"Y:="			, "0mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox1",
				"Y:="			, "spacey*ratioy1",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox1",
				"Y:="			, "spacey*ratioy1",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox1",
				"Y:="			, "-spacey*ratioy1",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox2",
				"Y:="			, "-spacey*ratioy1",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox2",
				"Y:="			, "spacey*ratioy2+w2/2",
				"Z:="			, "0mm"
			]
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "turn1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"turn1:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "w1"
				],
				[
					"NAME:Height",
					"Value:="		, "height"
				]
			]
		]
	])


# Make turn2

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox2",
				"Y:="			, "0mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox2",
				"Y:="			, "spacey*ratioy2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox2",
				"Y:="			, "spacey*ratioy2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox2",
				"Y:="			, "-spacey*ratioy2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox3",
				"Y:="			, "-spacey*ratioy2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox3",
				"Y:="			, "spacey*ratioy3+w3/2",
				"Z:="			, "0mm"
			]
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "turn2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"turn2:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "w2"
				],
				[
					"NAME:Height",
					"Value:="		, "height"
				]
			]
		]
	])


# Make turn3

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox3",
				"Y:="			, "0mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox3",
				"Y:="			, "spacey*ratioy3",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox3",
				"Y:="			, "spacey*ratioy3",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox3",
				"Y:="			, "-spacey*ratioy3",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox4",
				"Y:="			, "-spacey*ratioy3",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox4",
				"Y:="			, "spacey*ratioy4+w4/2",
				"Z:="			, "0mm"
			]
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "turn3",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"turn3:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "w3"
				],
				[
					"NAME:Height",
					"Value:="		, "height"
				]
			]
		]
	])

# Make turn4

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox4",
				"Y:="			, "0mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox4",
				"Y:="			, "spacey*ratioy4",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox4",
				"Y:="			, "spacey*ratioy4",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox4",
				"Y:="			, "-spacey*ratioy4",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox5",
				"Y:="			, "-spacey*ratioy4",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox5",
				"Y:="			, "spacey*ratioy5+w5/2",
				"Z:="			, "0mm"
			]
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "turn4",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"turn4:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "w4"
				],
				[
					"NAME:Height",
					"Value:="		, "height"
				]
			]
		]
	])


# Make turn5

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox5",
				"Y:="			, "0mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox5",
				"Y:="			, "spacey*ratioy5",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox5",
				"Y:="			, "spacey*ratioy5",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox5",
				"Y:="			, "-spacey*ratioy5",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox6",
				"Y:="			, "-spacey*ratioy5",
				"Z:="			, "0mm"
			]
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "turn5",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"turn5:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "w5"
				],
				[
					"NAME:Height",
					"Value:="		, "height"
				]
			]
		]
	])


# Make sheet
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox1+width/2",
				"Y:="			, "-spacey*ratioy5-width*2+width/2",
				"Z:="			, "-2mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox6-w5/2",
				"Y:="			, "-spacey*ratioy5-width*2+width/2",
				"Z:="			, "0mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "lumped",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"lumped:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "width"
				]
			]
		]
	])

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "(spacex*ratiox1+width/2+spacex*ratiox6-w5/2)/2",
				"Y:="			, "(-spacey*ratioy5-width*2+width/2-spacey*ratioy5-width*2+width/2)/2",
				"Z:="			, "(-2mm+0mm)/2"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox6-w5/2",
				"Y:="			, "-spacey*ratioy5-width*2+width/2",
				"Z:="			, "0mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "terminal",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"terminal:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "width"
				]
			]
		]
	])


oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Box,Ter1,Ter2,turn1,turn2,turn3,turn4,turn5"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])

# boundary setup
oModule = oDesign.GetModule("BoundarySetup")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oFaceIDs1 = oEditor.GetFaceIDs("lumped")
oFaceIDs2 = oEditor.GetFaceIDs("terminal")

oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		oFaceIDs1[0]
	], False, 
	[
		"NAME:ReferenceConductors", 
		"Box"
	], "1", True)
oModule.AssignTerminal(
	[
		"NAME:Ter1",
		"Objects:="		, ["terminal"],
		"ParentBndID:="		, "1",
		"TerminalResistance:="	, "50ohm"
	])


oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "$freqkHz",
		"MaxDeltaS:="		, 1e-12,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 15,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])
oProject.Save()
oDesign.Analyze("Setup1")



oModule = oDesign.GetModule("FieldsReporter")
oModule.CalcStack("clear")
oModule.EnterQty("H")
oModule.CalcOp("Mag")
oModule.ExportOnGrid(address1+"\\data_temp\\Hfield1.fld", ["-127/128*magx", "-127/128*magy", "1mm"], ["127/128*magx", "127/128*magy", "10mm"], ["magx/64", "magy/64", "1mm"], "Setup1 : LastAdaptive", 
	
	[
		"Freq:="		, "$freqkHz",
		"N1:="			, "$N1",
		"Phase:="		, "0deg",
		"airx:="		, "spacex*ratiox6*2.5",
		"airy:="		, "spacey*ratioy5*3",
		"airz:="		, "50mm",
		"height:="		, "34.2um",
		"magx:="		, "spacex*ratiox5",
		"magy:="		, "spacey*ratioy5",
		"ratiox1:="		, "$ratiox1",
		"ratiox2:="		, "$ratiox2",
		"ratiox3:="		, "$ratiox3",
		"ratiox4:="		, "$ratiox4",
		"ratiox5:="		, "$ratiox5",
		"ratiox6:="		, "$ratiox6",
		"ratioy1:="		, "$ratioy1",
		"ratioy2:="		, "$ratioy2",
		"ratioy3:="		, "$ratioy3",
		"ratioy4:="		, "$ratioy4",
		"ratioy5:="		, "$ratioy5",
		"spacex:="		, "$spacexmm",
		"spacey:="		, "$spaceymm",
		"w1:="			, "$w1mm",
		"w2:="			, "$w2mm",
		"w3:="			, "$w3mm",
		"w4:="			, "$w4mm",
		"w5:="			, "$w5mm",
		"width:="		, "$w1mm"
	], True, "Cartesian", ["0mm", "0mm", "0mm"], False)

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Terminal Z Parameter Table 1", "Terminal Solution Data", "Data Table", "Setup1 : LastAdaptive", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"N1:="			, ["Nominal"],
		"width:="		, ["Nominal"],
		"w1:="			, ["Nominal"],
		"w2:="			, ["Nominal"],
		"w3:="			, ["Nominal"],
		"w4:="			, ["Nominal"],
		"w5:="			, ["Nominal"],
		"spacex:="		, ["Nominal"],
		"spacey:="		, ["Nominal"],
		"ratiox1:="		, ["Nominal"],
		"ratiox2:="		, ["Nominal"],
		"ratiox3:="		, ["Nominal"],
		"ratiox4:="		, ["Nominal"],
		"ratiox5:="		, ["Nominal"],
		"ratiox6:="		, ["Nominal"],
		"ratioy1:="		, ["Nominal"],
		"ratioy2:="		, ["Nominal"],
		"ratioy3:="		, ["Nominal"],
		"ratioy4:="		, ["Nominal"],
		"ratioy5:="		, ["Nominal"],
		"airz:="		, ["Nominal"],
		"height:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["re(Zt(Ter1,Ter1))","im(Zt(Ter1,Ter1))/2/pi/freq*1e+6"]
	])
oModule.ExportToFile("Terminal Z Parameter Table 1", address2+"/data_temp/RLdata1.csv", False)




# simul 2

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
				"NAME:ChangedProps",
				[
					"NAME:w1",
					"Value:="		, "$X2w1mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w2",
					"Value:="		, "$X2w2mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w3",
					"Value:="		, "$X2w3mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w4",
					"Value:="		, "$X2w4mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w5",
					"Value:="		, "$X2w5mm"
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
				"NAME:ChangedProps",
				[
					"NAME:spacex",
					"Value:="		, "$X2spacexmm"
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
				"NAME:ChangedProps",
				[
					"NAME:spacey",
					"Value:="		, "$X2spaceymm"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox1",
					"Value:="		, "$X2ratiox1"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox2",
					"Value:="		, "$X2ratiox2"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox3",
					"Value:="		, "$X2ratiox3"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox4",
					"Value:="		, "$X2ratiox4"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox5",
					"Value:="		, "$X2ratiox5"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox6",
					"Value:="		, "$X2ratiox6"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy1",
					"Value:="		, "$X2ratioy1"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy2",
					"Value:="		, "$X2ratioy2"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy3",
					"Value:="		, "$X2ratioy3"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy4",
					"Value:="		, "$X2ratioy4"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy5",
					"Value:="		, "$X2ratioy5"
				]
			]
		]
	])


oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "$X2freqkHz",
		"MaxDeltaS:="		, 1e-12,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 15,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])
oProject.Save()
oDesign.Analyze("Setup1")



oModule = oDesign.GetModule("FieldsReporter")
oModule.CalcStack("clear")
oModule.EnterQty("H")
oModule.CalcOp("Mag")
oModule.ExportOnGrid(address1+"\\data_temp\\Hfield2.fld", ["-127/128*magx", "-127/128*magy", "1mm"], ["127/128*magx", "127/128*magy", "10mm"], ["magx/64", "magy/64", "1mm"], "Setup1 : LastAdaptive", 
	
	[
		"Freq:="		, "$X2freqkHz",
		"N1:="			, "$N1",
		"Phase:="		, "0deg",
		"airx:="		, "spacex*ratiox6*2.5",
		"airy:="		, "spacey*ratioy5*3",
		"airz:="		, "50mm",
		"height:="		, "34.2um",
		"magx:="		, "spacex*ratiox5",
		"magy:="		, "spacey*ratioy5",
		"ratiox1:="		, "$X2ratiox1",
		"ratiox2:="		, "$X2ratiox2",
		"ratiox3:="		, "$X2ratiox3",
		"ratiox4:="		, "$X2ratiox4",
		"ratiox5:="		, "$X2ratiox5",
		"ratiox6:="		, "$X2ratiox6",
		"ratioy1:="		, "$X2ratioy1",
		"ratioy2:="		, "$X2ratioy2",
		"ratioy3:="		, "$X2ratioy3",
		"ratioy4:="		, "$X2ratioy4",
		"ratioy5:="		, "$X2ratioy5",
		"spacex:="		, "$X2spacexmm",
		"spacey:="		, "$X2spaceymm",
		"w1:="			, "$X2w1mm",
		"w2:="			, "$X2w2mm",
		"w3:="			, "$X2w3mm",
		"w4:="			, "$X2w4mm",
		"w5:="			, "$X2w5mm",
		"width:="		, "$X2w1mm"
	], True, "Cartesian", ["0mm", "0mm", "0mm"], False)

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Terminal Z Parameter Table 1", address2+"/data_temp/RLdata2.csv", False)


# simul 3

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
				"NAME:ChangedProps",
				[
					"NAME:w1",
					"Value:="		, "$X3w1mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w2",
					"Value:="		, "$X3w2mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w3",
					"Value:="		, "$X3w3mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w4",
					"Value:="		, "$X3w4mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w5",
					"Value:="		, "$X3w5mm"
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
				"NAME:ChangedProps",
				[
					"NAME:spacex",
					"Value:="		, "$X3spacexmm"
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
				"NAME:ChangedProps",
				[
					"NAME:spacey",
					"Value:="		, "$X3spaceymm"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox1",
					"Value:="		, "$X3ratiox1"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox2",
					"Value:="		, "$X3ratiox2"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox3",
					"Value:="		, "$X3ratiox3"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox4",
					"Value:="		, "$X3ratiox4"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox5",
					"Value:="		, "$X3ratiox5"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox6",
					"Value:="		, "$X3ratiox6"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy1",
					"Value:="		, "$X3ratioy1"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy2",
					"Value:="		, "$X3ratioy2"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy3",
					"Value:="		, "$X3ratioy3"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy4",
					"Value:="		, "$X3ratioy4"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy5",
					"Value:="		, "$X3ratioy5"
				]
			]
		]
	])


oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "$X3freqkHz",
		"MaxDeltaS:="		, 1e-12,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 15,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])
oProject.Save()
oDesign.Analyze("Setup1")



oModule = oDesign.GetModule("FieldsReporter")
oModule.CalcStack("clear")
oModule.EnterQty("H")
oModule.CalcOp("Mag")
oModule.ExportOnGrid(address1+"\\data_temp\\Hfield3.fld", ["-127/128*magx", "-127/128*magy", "1mm"], ["127/128*magx", "127/128*magy", "10mm"], ["magx/64", "magy/64", "1mm"], "Setup1 : LastAdaptive", 
	
	[
		"Freq:="		, "$X3freqkHz",
		"N1:="			, "$N1",
		"Phase:="		, "0deg",
		"airx:="		, "spacex*ratiox6*2.5",
		"airy:="		, "spacey*ratioy5*3",
		"airz:="		, "50mm",
		"height:="		, "34.2um",
		"magx:="		, "spacex*ratiox5",
		"magy:="		, "spacey*ratioy5",
		"ratiox1:="		, "$X3ratiox1",
		"ratioX3:="		, "$X3ratiox2",
		"ratiox3:="		, "$X3ratiox3",
		"ratiox4:="		, "$X3ratiox4",
		"ratiox5:="		, "$X3ratiox5",
		"ratiox6:="		, "$X3ratiox6",
		"ratioy1:="		, "$X3ratioy1",
		"ratioy2:="		, "$X3ratioy2",
		"ratioy3:="		, "$X3ratioy3",
		"ratioy4:="		, "$X3ratioy4",
		"ratioy5:="		, "$X3ratioy5",
		"spacex:="		, "$X3spacexmm",
		"spacey:="		, "$X3spaceymm",
		"w1:="			, "$X3w1mm",
		"w2:="			, "$X3w2mm",
		"w3:="			, "$X3w3mm",
		"w4:="			, "$X3w4mm",
		"w5:="			, "$X3w5mm",
		"width:="		, "$X3w1mm"
	], True, "Cartesian", ["0mm", "0mm", "0mm"], False)

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Terminal Z Parameter Table 1", address2+"/data_temp/RLdata3.csv", False)


# simul 3

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
				"NAME:ChangedProps",
				[
					"NAME:w1",
					"Value:="		, "$X4w1mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w2",
					"Value:="		, "$X4w2mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w3",
					"Value:="		, "$X4w3mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w4",
					"Value:="		, "$X4w4mm"
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
				"NAME:ChangedProps",
				[
					"NAME:w5",
					"Value:="		, "$X4w5mm"
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
				"NAME:ChangedProps",
				[
					"NAME:spacex",
					"Value:="		, "$X4spacexmm"
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
				"NAME:ChangedProps",
				[
					"NAME:spacey",
					"Value:="		, "$X4spaceymm"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox1",
					"Value:="		, "$X4ratiox1"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox2",
					"Value:="		, "$X4ratiox2"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox3",
					"Value:="		, "$X4ratiox3"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox4",
					"Value:="		, "$X4ratiox4"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox5",
					"Value:="		, "$X4ratiox5"
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
				"NAME:ChangedProps",
				[
					"NAME:ratiox6",
					"Value:="		, "$X4ratiox6"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy1",
					"Value:="		, "$X4ratioy1"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy2",
					"Value:="		, "$X4ratioy2"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy3",
					"Value:="		, "$X4ratioy3"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy4",
					"Value:="		, "$X4ratioy4"
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
				"NAME:ChangedProps",
				[
					"NAME:ratioy5",
					"Value:="		, "$X4ratioy5"
				]
			]
		]
	])


oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"SolveType:="		, "Single",
		"Frequency:="		, "$X4freqkHz",
		"MaxDeltaS:="		, 1e-12,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 15,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])
oProject.Save()
oDesign.Analyze("Setup1")



oModule = oDesign.GetModule("FieldsReporter")
oModule.CalcStack("clear")
oModule.EnterQty("H")
oModule.CalcOp("Mag")
oModule.ExportOnGrid(address1+"\\data_temp\\Hfield4.fld", ["-127/128*magx", "-127/128*magy", "1mm"], ["127/128*magx", "127/128*magy", "10mm"], ["magx/64", "magy/64", "1mm"], "Setup1 : LastAdaptive", 
	
	[
		"Freq:="		, "$X4freqkHz",
		"N1:="			, "$N1",
		"Phase:="		, "0deg",
		"airx:="		, "spacex*ratiox6*2.5",
		"airy:="		, "spacey*ratioy5*3",
		"airz:="		, "50mm",
		"height:="		, "34.2um",
		"magx:="		, "spacex*ratiox5",
		"magy:="		, "spacey*ratioy5",
		"ratiox1:="		, "$X4ratiox1",
		"ratioX4:="		, "$X4ratiox2",
		"ratioX4:="		, "$X4ratiox3",
		"ratiox4:="		, "$X4ratiox4",
		"ratiox5:="		, "$X4ratiox5",
		"ratiox6:="		, "$X4ratiox6",
		"ratioy1:="		, "$X4ratioy1",
		"ratioy2:="		, "$X4ratioy2",
		"ratioy3:="		, "$X4ratioy3",
		"ratioy4:="		, "$X4ratioy4",
		"ratioy5:="		, "$X4ratioy5",
		"spacex:="		, "$X4spacexmm",
		"spacey:="		, "$X4spaceymm",
		"w1:="			, "$X4w1mm",
		"w2:="			, "$X4w2mm",
		"w3:="			, "$X4w3mm",
		"w4:="			, "$X4w4mm",
		"w5:="			, "$X4w5mm",
		"width:="		, "$X4w1mm"
	], True, "Cartesian", ["0mm", "0mm", "0mm"], False)

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Terminal Z Parameter Table 1", address2+"/data_temp/RLdata4.csv", False)