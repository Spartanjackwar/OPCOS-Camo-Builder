//xxx replace will change classnames and filenames.
//yyy replace will change filepaths.
//zzz replace will change display names.
//www replace will change prefix names.
//Note!  The sniper uses woodland default helmet since you can't really see through the ghillie
//Note!  The officer uses the default patrol cap
//Note!  The crewman uses the default NATO crew helm
/*
class CfgEditorSubcategories
{
	class www_3DENSUBCAT_Men_xxx
	{
		displayName = "Men (zzz)";
	};
};
*/

//class CfgVehicles
//{
	/*
	class OPTRE_UNSC_Army_Soldier_AA_Specialist_WDL;
	class OPTRE_UNSC_Army_Soldier_Assist_Autorifleman_WDL;
	class OPTRE_UNSC_Army_Soldier_AT_Specialist_WDL;
	class OPTRE_UNSC_Army_Soldier_Autorifleman_WDL;
	class OPTRE_UNSC_Army_Soldier_Breacher_WDL;
	class OPTRE_UNSC_Army_Soldier_Crewman_WDL;
	class OPTRE_UNSC_Army_Soldier_Demolitions_WDL;
	class OPTRE_UNSC_Army_Soldier_Marksman_WDL;
	class OPTRE_UNSC_Army_Soldier_Engineer_WDL;
	class OPTRE_UNSC_Army_Soldier_ForwardObserver_WDL;
	class OPTRE_UNSC_Army_Soldier_Grenadier_WDL;
	class OPTRE_UNSC_Army_Soldier_Officer_WDL;
	class OPTRE_UNSC_Army_Soldier_Medic_WDL;
	class OPTRE_UNSC_Army_Soldier_Radioman_WDL;
	class OPTRE_UNSC_Army_Soldier_Rifleman_AT_WDL;
	class OPTRE_UNSC_Army_Soldier_Rifleman_BR_WDL;
	class OPTRE_UNSC_Army_Soldier_Rifleman_Light_WDL;
	class OPTRE_UNSC_Army_Soldier_Rifleman_AR_WDL;
	class OPTRE_UNSC_Army_Soldier_Sniper_WDL;
	class OPTRE_UNSC_Army_Soldier_SquadLead_WDL;
	class OPTRE_UNSC_Army_Soldier_TeamLead_WDL;
	class OPTRE_UNSC_Army_Soldier_UAV_Op_WDL;
	class OPTRE_UNSC_Army_Soldier_Unarmed_WDL;
	*/
	
	class www_UNSC_Army_Soldier_AA_Specialist_xxx: OPTRE_UNSC_Army_Soldier_AA_Specialist_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Assist_Autorifleman_xxx: OPTRE_UNSC_Army_Soldier_Assist_Autorifleman_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_AT_Specialist_xxx: OPTRE_UNSC_Army_Soldier_AT_Specialist_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Autorifleman_xxx: OPTRE_UNSC_Army_Soldier_Autorifleman_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx_slimleg";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_MG_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_MG_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Breacher_xxx: OPTRE_UNSC_Army_Soldier_Breacher_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx_slimleg";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Breacher_WDL", "OPTRE_UNSC_CH252_Helmet_Vacuum_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Breacher_WDL", "OPTRE_UNSC_CH252_Helmet_Vacuum_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Crewman_xxx: OPTRE_UNSC_Army_Soldier_Crewman_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor3_WDL", "H_HelmetCrew_B", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor3_WDL", "H_HelmetCrew_B", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Demolitions_xxx: OPTRE_UNSC_Army_Soldier_Demolitions_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Marksman_xxx: OPTRE_UNSC_Army_Soldier_Marksman_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Marksman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Marksman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Engineer_xxx: OPTRE_UNSC_Army_Soldier_Engineer_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_ForwardObserver_xxx: OPTRE_UNSC_Army_Soldier_ForwardObserver_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Grenadier_xxx: OPTRE_UNSC_Army_Soldier_Grenadier_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Grenadier_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Grenadier_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Officer_xxx: OPTRE_UNSC_Army_Soldier_Officer_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx_S";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_PatrolCap_Army", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_PatrolCap_Army", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Medic_xxx: OPTRE_UNSC_Army_Soldier_Medic_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Medic_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL_MED", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Medic_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL_MED", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Radioman_xxx: OPTRE_UNSC_Army_Soldier_Radioman_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Rifleman_AT_xxx: OPTRE_UNSC_Army_Soldier_Rifleman_AT_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Rifleman_BR_xxx: OPTRE_UNSC_Army_Soldier_Rifleman_BR_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Marksman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Marksman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Rifleman_Light_xxx: OPTRE_UNSC_Army_Soldier_Rifleman_Light_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx_S";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor3_WDL", "OPTRE_UNSC_Watchcap", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor3_WDL", "OPTRE_UNSC_Watchcap", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Rifleman_AR_xxx: OPTRE_UNSC_Army_Soldier_Rifleman_AR_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Rifleman_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_Sniper_xxx: OPTRE_UNSC_Army_Soldier_Sniper_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_Sniper_WDL", "OPTRE_UNSC_CH252_Helmet3_wdl", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_Sniper_WDL", "OPTRE_UNSC_CH252_Helmet3_wdl", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_SquadLead_xxx: OPTRE_UNSC_Army_Soldier_SquadLead_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet2_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_TeamLead_xxx: OPTRE_UNSC_Army_Soldier_TeamLead_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
	class www_UNSC_Army_Soldier_UAV_Op_xxx: OPTRE_UNSC_Army_Soldier_UAV_Op_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG", "B_UavTerminal"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor_TL_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG", "B_UavTerminal"};
	};
	class www_UNSC_Army_Soldier_Unarmed_xxx: OPTRE_UNSC_Army_Soldier_Unarmed_WDL
	{
		dlc = "www";
		author = "Spartanjackwar";
		side = 1;
		editorCategory = "www_3DENCAT_Men_UNSC";
		editorSubcategory = "www_3DENSUBCAT_Men_xxx";
		faction = "OPTRE_UNSC";
		
		uniformClass = "www_UNSC_Army_Uniform_xxx_R";
		linkedItems[] = {"OPTRE_UNSC_M52A_Armor3_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
		respawnLinkedItems[] = {"OPTRE_UNSC_M52A_Armor3_WDL", "OPTRE_UNSC_CH252_Helmet_WDL", "ItemMap", "ItemCompass", "ItemWatch", "ItemRadio", "OPTRE_Biofoam", "OPTRE_NVG"};
	};
//};

//The following goes in the cfgPatches units[] = {};
/*
"www_UNSC_Army_Soldier_AA_Specialist_WDL",
"www_UNSC_Army_Soldier_Assist_Autorifleman_WDL",
"www_UNSC_Army_Soldier_AT_Specialist_WDL",
"www_UNSC_Army_Soldier_Autorifleman_WDL",
"www_UNSC_Army_Soldier_Breacher_WDL",
"www_UNSC_Army_Soldier_Crewman_WDL",
"www_UNSC_Army_Soldier_Demolitions_WDL",
"www_UNSC_Army_Soldier_Marksman_WDL",
"www_UNSC_Army_Soldier_Engineer_WDL",
"www_UNSC_Army_Soldier_ForwardObserver_WDL",
"www_UNSC_Army_Soldier_Grenadier_WDL",
"www_UNSC_Army_Soldier_Officer_WDL",
"www_UNSC_Army_Soldier_Medic_WDL",
"www_UNSC_Army_Soldier_Radioman_WDL",
"www_UNSC_Army_Soldier_Rifleman_AT_WDL",
"www_UNSC_Army_Soldier_Rifleman_BR_WDL",
"www_UNSC_Army_Soldier_Rifleman_Light_WDL",
"www_UNSC_Army_Soldier_Rifleman_AR_WDL",
"www_UNSC_Army_Soldier_Sniper_WDL",
"www_UNSC_Army_Soldier_SquadLead_WDL",
"www_UNSC_Army_Soldier_TeamLead_WDL",
"www_UNSC_Army_Soldier_UAV_Op_WDL",
"www_UNSC_Army_Soldier_Unarmed_WDL",
*/