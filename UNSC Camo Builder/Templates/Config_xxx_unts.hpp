//Jack Moss

class CfgPatches
{
 	class WWW_XXX
 	{
		author = "Spartanjackwar";
 		requiredAddons[] = {
			"A3_Weapons_F", "A3_characters_f_bootcamp", "A3_Characters_F",
			
			"OPTRE_Core", "OPTRE_UNSC_Units", "OPTRE_UNSC_Units_Army",
			
			"OPCOS_CORE"
		};
 		units[] = {
			#include<UnitList.hpp>
		};
 		weapons[] = {};
		magazines[] = {};
		ammo[] = {};
 		requiredVersion = 0.1;
 	};
};

class CfgEditorCategories
{
	class OPCOS_3DENCAT_UNSC
	{
		displayName = "UNSCDF (OPCOS)";
	};
	class OPCOS_3DENCAT_Police
	{
		displayName = "UNSC Police (OPCOS)";
	};
	class OPCOS_3DENCAT_INS
	{
		displayName = "Insurrectionists (OPCOS)";
	};
};

class CfgEditorSubcategories
{
	#include<CfG3densubcats.hpp>
};

class cfgVehicles
{
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
	
	#include<CfgVehicle.hpp>
};