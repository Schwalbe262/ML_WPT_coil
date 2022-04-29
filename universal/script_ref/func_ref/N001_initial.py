import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

address1 = "Z:\\git\\ML_WPT_coil\\universal\\script1"
address2 = "Z:\ML_WPT\ML_WPT_coil\script1"


# Open aedt file
oDesktop.OpenProject("./ML_aedt/ML1.aedt")


# Make project
oProject = oDesktop.SetActiveProject("ML1")
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

