# Make turn8

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox8",
				"Y:="			, "0mm",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox8",
				"Y:="			, "spacey*ratioy8",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox8",
				"Y:="			, "spacey*ratioy8",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-spacex*ratiox8",
				"Y:="			, "-spacey*ratioy8",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "spacex*ratiox9",
				"Y:="			, "-spacey*ratioy8",
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
		"Name:="		, "turn8",
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
					"Value:="		, "w8"
				],
				[
					"NAME:Height",
					"Value:="		, "height"
				]
			]
		]
	])