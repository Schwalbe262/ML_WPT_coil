import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("Y:/git/ML_WPT_coil/LRT/simple_model_turn22/script8/ML_aedt/ML8.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML8")
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
		"MaximumPasses:="	, 10,
		"MinimumPasses:="	, 10,
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
					"Value:="		, "100mm"
					
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
					"Value:="		, "[0, 0]"
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
					"Value:="		, "[15, 15] mm"
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
					"Value:="		, "[$ferrite_thick0, $ferrite_thick1] mm"
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
					"NAME:ferrite_height",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$ferrite_height0, $ferrite_height1] mm"
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
					"NAME:ferrite_ex",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$ferrite_ex0, $ferrite_ex1]mm"
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
					"NAME:ferrite_margin",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$ferrite_margin0, $ferrite_margin1]mm"
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



# Make air
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-(width[0]+width[1])",
		"YPosition:="		, "-(height[0]+height[1])/2",
		"ZPosition:="		, "-150mm-air_gap/2",
		"XSize:="		, "(width[0]+width[1])*2",
		"YSize:="		, "(height[0]+height[1])",
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
		"XPosition:="		, "-width[0]/2-coil_width[0]/2-(ferrite_ex[0]+ferrite_margin[0])",
		"YPosition:="		, "-height[0]/2-coil_width[0]/2-(ferrite_ex[0]+ferrite_margin[0])",
		"ZPosition:="		, "-air_gap/2-coil_width[0]/2+ferrite_height[0]",
		"XSize:="		, "width[0]+coil_width[0]+2*(ferrite_ex[0]+ferrite_margin[0])",
		"YSize:="		, "height[0]+coil_width[0]+2*(ferrite_ex[0]+ferrite_margin[0])",
		"ZSize:="		, "-ferrite_thick[0]-ferrite_height[0]"
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
		"XPosition:="		, "-width[0]/2-coil_width[0]/2-ferrite_margin[0]",
		"YPosition:="		, "-height[0]/2-coil_width[0]/2-ferrite_margin[0]",
		"ZPosition:="		, "-air_gap/2-coil_width[0]/2",
		"XSize:="		, "width[0]+coil_width[0]+2*ferrite_margin[0]",
		"YSize:="		, "height[0]+coil_width[0]+2*ferrite_margin[0]",
		"ZSize:="		, "ferrite_height[0]"
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

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-width[0]/2-coil_width[0]/2-ferrite_margin[0]",
		"YPosition:="		, "height[0]/2+coil_width[0]/2+ferrite_margin[0]+ferrite_ex[0]",
		"ZPosition:="		, "-air_gap/2-coil_width[0]/2",
		"XSize:="		, "3*(gap[0]+coil_width[0])+ferrite_margin[0]",
		"YSize:="		, "-ferrite_ex[0]",
		"ZSize:="		, "ferrite_height[0]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_tx_sub2",
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
		"Tool Parts:="		, "ferrite_tx_sub,ferrite_tx_sub2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])



oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-width[1]/2-coil_width[1]/2-ferrite_ex[1]-ferrite_margin[1]",
		"YPosition:="		, "-height[1]/2-coil_width[1]/2-ferrite_ex[1]-ferrite_margin[1]",
		"ZPosition:="		, "air_gap/2+coil_width[1]/2-ferrite_height[1]",
		"XSize:="		, "width[1]+coil_width[1]+2*(ferrite_ex[1]+ferrite_margin[1])",
		"YSize:="		, "height[1]+coil_width[1]+2*(ferrite_ex[1]+ferrite_margin[1])",
		"ZSize:="		, "ferrite_thick[1]+ferrite_height[1]"
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
		"XPosition:="		, "-width[1]/2-coil_width[1]/2-ferrite_margin[1]",
		"YPosition:="		, "-height[1]/2-coil_width[1]/2-ferrite_margin[1]",
		"ZPosition:="		, "air_gap/2+coil_width[1]/2",
		"XSize:="		, "width[1]+coil_width[1]+2*ferrite_margin[1]",
		"YSize:="		, "height[1]+coil_width[1]+2*ferrite_margin[1]",
		"ZSize:="		, "-ferrite_height[1]"
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

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "width[1]/2+coil_width[1]/2+ferrite_margin[1]",
		"YPosition:="		, "-height[1]/2-coil_width[1]/2-ferrite_margin[1]-ferrite_ex[1]",
		"ZPosition:="		, "air_gap/2+coil_width[1]/2",
		"XSize:="		, "-3*(gap[1]+coil_width[1])-ferrite_margin[1]",
		"YSize:="		, "ferrite_ex[1]",
		"ZSize:="		, "-ferrite_height[1]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_rx_sub2",
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
		"Tool Parts:="		, "ferrite_rx_sub,ferrite_rx_sub2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])


oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "ferrite_rx",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "-width[0]*move[0]",
		"TranslateVectorY:="	, "-height[0]*move[1]",
		"TranslateVectorZ:="	, "0mm"
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
				"Y:="			, "(height[0]+height[1])/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]",
				"Y:="			, "1/2*height[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]",
				"Y:="			, "-1/2*height[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "1/2*width[0]",
				"Y:="			, "-1/2*height[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "1/2*width[0]",
				"Y:="			, "1/2*height[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+1*(gap[0]+coil_width[0])",
				"Y:="			, "1/2*height[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+1*(gap[0]+coil_width[0])",
				"Y:="			, "1/2*height[0]-1*(gap[0]+coil_width[0])",
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
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx1",
		"Flags:="		, "",
		"Color:="		, "(255 0 0)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])



oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+1*(gap[0]+coil_width[0])",
				"Y:="			, "1/2*height[0]+0*(gap[0]+coil_width[0])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+1*(gap[0]+coil_width[0])",
				"Y:="			, "-1/2*height[0]+1*(gap[0]+coil_width[0])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "1/2*width[0]-1*(gap[0]+coil_width[0])",
				"Y:="			, "-1/2*height[0]+1*(gap[0]+coil_width[0])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "1/2*width[0]-1*(gap[0]+coil_width[0])",
				"Y:="			, "1/2*height[0]-1*(gap[0]+coil_width[0])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+2*(gap[0]+coil_width[0])",
				"Y:="			, "1/2*height[0]-1*(gap[0]+coil_width[0])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+2*(gap[0]+coil_width[0])",
				"Y:="			, "1/2*height[0]-1*(gap[0]+coil_width[0])",
				"Z:="			, "coil_width[0]+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+2*(gap[0]+coil_width[0])",
				"Y:="			, "1/2*height[0]+1*(gap[0]+coil_width[0])",
				"Z:="			, "coil_width[0]+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+2*(gap[0]+coil_width[0])",
				"Y:="			, "1/2*height[0]+1*(gap[0]+coil_width[0])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1/2*width[0]+2*(gap[0]+coil_width[0])",
				"Y:="			, "(height[0]+height[1])/2",
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx2",
		"Flags:="		, "",
		"Color:="		, "(255 0 0)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Tx1,Tx2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])


oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "-air_gap/2"
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
				"X:="			, "-width[1]/2",
				"Y:="			, "0.5*(height[0]+height[1])-height[0]*move[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2",
				"Y:="			, "height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2",
				"Y:="			, "-height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[1]/2",
				"Y:="			, "-height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[1]/2",
				"Y:="			, "height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+1*(gap[1]+coil_width[1])",
				"Y:="			, "height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+1*(gap[1]+coil_width[1])",
				"Y:="			, "height[1]/2-1*(gap[1]+coil_width[1])",
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
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[1]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx1",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])



oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+1*(gap[1]+coil_width[1])",
				"Y:="			, "height[1]/2+0*(gap[1]+coil_width[1])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+1*(gap[1]+coil_width[1])",
				"Y:="			, "-height[1]/2+1*(gap[1]+coil_width[1])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[1]/2-1*(gap[1]+coil_width[1])",
				"Y:="			, "-height[1]/2+1*(gap[1]+coil_width[1])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[1]/2-1*(gap[1]+coil_width[1])",
				"Y:="			, "height[1]/2-1*(gap[1]+coil_width[1])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*(gap[1]+coil_width[1])",
				"Y:="			, "height[1]/2-1*(gap[1]+coil_width[1])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*(gap[1]+coil_width[1])",
				"Y:="			, "height[1]/2-1*(gap[1]+coil_width[1])",
				"Z:="			, "coil_width[1]+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*(gap[1]+coil_width[1])",
				"Y:="			, "height[1]/2+1*(gap[1]+coil_width[1])",
				"Z:="			, "coil_width[1]+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*(gap[1]+coil_width[1])",
				"Y:="			, "height[1]/2+1*(gap[1]+coil_width[1])",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*(gap[1]+coil_width[1])",
				"Y:="			, "(height[0]+height[1])/2-height[0]*move[1]",
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[1]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx2",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1,Rx2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])


oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "width[0]*move[0]",
		"TranslateVectorY:="	, "height[0]*move[1]",
		"TranslateVectorZ:="	, "-air_gap/2"
	])






oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		, "0mm",
		"MirrorBaseY:="		, "0mm",
		"MirrorBaseZ:="		, "0mm",
		"MirrorNormalX:="	, "0mm",
		"MirrorNormalY:="	, "1mm",
		"MirrorNormalZ:="	, "0mm"
	])

oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		, "0mm",
		"MirrorBaseY:="		, "0mm",
		"MirrorBaseZ:="		, "0mm",
		"MirrorNormalX:="	, "1mm",
		"MirrorNormalY:="	, "0mm",
		"MirrorNormalZ:="	, "0mm"
	])

oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		, "0mm",
		"MirrorBaseY:="		, "0mm",
		"MirrorBaseZ:="		, "0mm",
		"MirrorNormalX:="	, "0mm",
		"MirrorNormalY:="	, "0mm",
		"MirrorNormalZ:="	, "1mm"
	])



# Tx Make sheet

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "-1/2*width[0]",
		"YCenter:="		, "(height[0]+height[1])/2",
		"ZCenter:="		, "-air_gap/2",
		"XStart:="		, "-1/2*width[0]",
		"YStart:="		, "(height[0]+height[1])/2",
		"ZStart:="		, "-air_gap/2+coil_width[0]/2",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_in",
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


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "-1/2*width[0]+2*(gap[0]+coil_width[0])",
		"YCenter:="		, "(height[0]+height[1])/2",
		"ZCenter:="		, "-air_gap/2",
		"XStart:="		, "-1/2*width[0]+2*(gap[0]+coil_width[0])+coil_width[0]/2",
		"YStart:="		, "(height[0]+height[1])/2",
		"ZStart:="		, "-air_gap/2",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out",
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


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "1/2*width[1]-width[0]*move[0]",
		"YCenter:="		, "-(height[0]+height[1])/2",
		"ZCenter:="		, "air_gap/2",
		"XStart:="		, "1/2*width[1]-width[0]*move[0]",
		"YStart:="		, "-(height[0]+height[1])/2",
		"ZStart:="		, "air_gap/2-coil_width[1]/2",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_in",
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


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "1/2*width[1]-width[0]*move[0]-2*(gap[1]+coil_width[1])",
		"YCenter:="		, "-(height[0]+height[1])/2",
		"ZCenter:="		, "air_gap/2",
		"XStart:="		, "1/2*width[1]-width[0]*move[0]-2*(gap[1]+coil_width[1])-coil_width[1]/2",
		"YStart:="		, "-(height[0]+height[1])/2",
		"ZStart:="		, "air_gap/2",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_out",
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




# Set coil terminal

oModule = oDesign.GetModule("BoundarySetup")

oModule.AssignCoilTerminal(
	[
		"NAME:Tx_in",
		"Objects:="		, ["Tx_in"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", False
	])

oModule.AssignCoilTerminal(
	[
		"NAME:Tx_out",
		"Objects:="		, ["Tx_out"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", True
	])


oModule.AssignCoilTerminal(
	[
		"NAME:Rx_in",
		"Objects:="		, ["Rx_in"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", False
	])

oModule.AssignCoilTerminal(
	[
		"NAME:Rx_out",
		"Objects:="		, ["Rx_out"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", True
	])


# Add winding

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWindingGroup(
	[
		"NAME:Tx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "100*sqrt(2)A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])

oModule.AssignWindingGroup(
	[
		"NAME:Rx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "100*sqrt(2)A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])




# Assign coil terminal


oModule.AddWindingTerminals("Tx", ["Tx_in", "Tx_out"])

oModule.AddWindingTerminals("Rx", ["Rx_in", "Rx_out"])


oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation(
	[
		"NAME:Radiation1",
		"Objects:="		, ["Air"]
	])


oModule = oDesign.GetModule("MaxwellParameterSetup")
oModule.AssignMatrix(
	[
		"NAME:Matrix1",
		[
			"NAME:MatrixEntry",
			[
				"NAME:MatrixEntry",
				"Source:="		, "Tx"
			],
			[
				"NAME:MatrixEntry",
				"Source:="		, "Rx"
			]
		]
	])


# Mesh setting

oModule = oDesign.GetModule("MeshSetup")
oModule.AssignSkinDepthOp(
	[
		"NAME:SkinDepth1",
		"Enabled:="		, True,
		"Objects:="		, ["Rx1","Tx1"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"SkinDepth:="		, "0.269794105765115mm",
		"SurfTriMaxLength:="	, "780.866025403785mm",
		"NumLayers:="		, "2"
	])


oProject.Save()
oDesign.Analyze("Setup1")




oModule = oDesign.GetModule("FieldsReporter")

oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Tx1")
oModule.CalcOp("Integrate")
oModule.EnterScalar(1)
oModule.CalcOp("*")
oModule.AddNamedExpression("Tx_loss", "Fields")

oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Rx1")
oModule.CalcOp("Integrate")
oModule.EnterScalar(1)
oModule.CalcOp("*")
oModule.AddNamedExpression("Rx_loss", "Fields")



oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("L Table 1", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air_gap:="		, ["Nominal"],
		"move:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Matrix1.L(Tx,Tx)","Matrix1.L(Rx,Rx)"]
	])




oModule.CreateReport("Coupling Coeff Table 1", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air_gap:="		, ["Nominal"],
		"move:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["-Matrix1.CplCoef(Tx,Rx)"]
	])


oModule.CreateReport("Calculator Expressions Table 1", "Fields", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air_gap:="		, ["Nominal"],
		"move:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Tx_loss","Rx_loss"]
	])

oModule.ExportToFile("L Table 1", "Y:/git/ML_WPT_coil/LRT/simple_model_turn22/script8/ML_data/inductance$VERSION_IDX_STR_dat.csv", False)
oModule.ExportToFile("Coupling Coeff Table 1", "Y:/git/ML_WPT_coil/LRT/simple_model_turn22/script8/ML_data/coupling$VERSION_IDX_STR_dat.csv", False)
oModule.ExportToFile("Calculator Expressions Table 1", "Y:/git/ML_WPT_coil/LRT/simple_model_turn22/script8/ML_data/loss$VERSION_IDX_STR_dat.csv", False)