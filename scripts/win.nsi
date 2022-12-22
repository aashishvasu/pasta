!include LogicLib.nsh

# Installer name
OutFile "pasta_installer_win.exe"

RequestExecutionLevel admin
ShowInstDetails show
ShowUninstDetails show

# Target installation directory
InstallDir "C:\pasta"

Page InstFiles

Unicode True

# default section start
Section

	# Output directory
	SetOutPath $INSTDIR

	# File to copy
	File ..\dist\pasta.exe

	# Create uninstaller at location
	WriteUninstaller $INSTDIR\Uninstall.exe

	# Local Machine access
	EnVar::SetHKLM

	# Check for write access
	EnVar::Check "NULL" "NULL"
	Pop $0
	DetailPrint "EnVar::Check write access HKLM returned=|$0|"

	# Check for env var Path
	EnVar::Check "Path" "NULL"
	Pop $0
	DetailPrint "EnVar::Check write access HKLM returned=|$0|"

	EnVar::Check "Path" "$INSTDIR"
	Pop $0
	${If} $0 = 0
		DetailPrint "Already exists at Path"
	${Else}
		EnVar::AddValue "Path" "$INSTDIR"
		Pop $0 ; 0 on success
	${EndIf}

# default section end
SectionEnd

Section "Uninstall"

	# Local Machine access
	EnVar::SetHKLM

	# Check for write access
	EnVar::Check "NULL" "NULL"
	Pop $0
	DetailPrint "EnVar::Check write access HKLM returned=|$0|"

	# Check for env var Path
	EnVar::Check "Path" "NULL"
	Pop $0
	DetailPrint "EnVar::Check write access HKLM returned=|$0|"

	EnVar::Check "Path" "$INSTDIR"
	Pop $0
	${If} $0 = 0
		# Remove directory location from Path env var
		EnVar::DeleteValue "Path" "$INSTDIR"
		Pop $0
		DetailPrint "EnVar::Check returned=|$0| (should be 0)"
	${EndIf}

	
	# Delete installed file
	Delete $INSTDIR\pasta.exe

	# Delete the uninstaller
	Delete $INSTDIR\Uninstall.exe

	# Delete the directory
	RMDir $INSTDIR

# Uninstall section end
SectionEnd