import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("Y:/git/ML_WPT_coil/LRT/HFSS_model_turn33_v1/script1/ML_aedt/ML1.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML1")
oDesign = oProject.SetActiveDesign("HFSS_ML_v$VERSION_IDX_STR") # check "HFSS_ML_v$VERSION_IDX_STR"


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
			"Magnitude:="		, "$Ltxe-6*2*pi*freq*$Itx*sqrt(2)V",
			"Phase:="		, "0deg"
		],
		[
			"Name:="		, "Ter_Rx",
			"Terminated:="		, False,
			"Magnitude:="		, "$Lrxe-6*2*pi*freq*$Irx*sqrt(2)V",
			"Phase:="		, "90deg"
		]
	])

oProject.Save()
oDesign.Analyze("Setup1")


oModule = oDesign.GetModule("FieldsReporter")
oModule.CopyNamedExprToStack("Surface_Loss_Density")
oModule.EnterSurf("Tx_coil")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Tx_loss", "Fields")
oModule.CopyNamedExprToStack("Surface_Loss_Density")
oModule.EnterSurf("Rx_coil")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Rx_loss", "Fields")


