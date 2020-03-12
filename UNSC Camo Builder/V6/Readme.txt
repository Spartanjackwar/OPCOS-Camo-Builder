1; script mode
2; template output mode
3; ini change mode
4; wipe file structure

1;scriptName;
2;classname;displayname;outputfilename;rootclass;
3;Section;Child;newvalue;
4;

rootclass will be ID'd with a W,M,A,V,3denSubcat,None,config for weapon, mag, ammo, vehicle, None, or config.cpp
if rootclass is Config, then the rest of the line is ignored.

//======================================================================================================
//Script Syntax Documentation, for your ease.
//======================================================================================================
//Mode number;Modname;ClassName;Display Name;TemplateFileName;Subfolder of \@Modname\Modname_units\;
//Scrip Mode: 	1;Filename of script
//Template Mode:2;classname;displayname;outputFileName;rootClassIdentifier;
//.ini change: 	3;Section;Child;NewValue;
//Reset folder: 4;

//Important notice!  Make sure every command ends with a semicolon!
//Failure to end commands in semicolons will introduce newline characters into parameters, which is bad.

//"rootClassIdentifier" is one of the following: W,M,A,V,3denSubcat,None,config.
//If the identifier is "Config", the rest of the line will be ignored.
//If the identifier is W, cfgWeapons.hpp will be appended a #include.
//If the identifier is M, cfgMagazines.hpp will be appended a #include.
//If the identifier is A, cfgAmmo.hpp will be appended a #include.
//If the identifier is V, cfgVehicles.hpp will be appended a #include.
//If the identifier is 3densubcat, cfg3densubcat.hpp will be appended a #include.
