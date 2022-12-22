# Installer name
OutFile "pasta_installer.exe"

# Target installation directory
InstallDir "C:\pasta"

# default section start
Section

	# Output directory
	SetOutPath $INSTDIR

	# File to copy
	File ..\dist\pasta.exe

	# Create uninstaller at location
    WriteUninstaller $INSTDIR\Uninstall.exe

# default section end
SectionEnd

Section "Uninstall"

	# Delete installed file
	Delete $INSTDIR\pasta.exe

	# Delete the uninstaller
	Delete $INSTDIR\Uninstall.exe

	# Delete the directory
	RMDir $INSTDIR

# Uninstall section end
SectionEnd