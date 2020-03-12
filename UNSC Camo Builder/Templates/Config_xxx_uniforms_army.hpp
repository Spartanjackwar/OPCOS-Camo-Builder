//Jack Moss + Rev!

class CfgPatches
{
 	class WWW_XXX
 	{
		author = "Rev! + Spartanjackwar";
 		requiredAddons[] = {
			"A3_Weapons_F", "A3_characters_f_bootcamp", "A3_Characters_F",
			"OPTRE_Core", "OPTRE_UNSC_Units", "OPTRE_UNSC_Units_Army",
			"OPCOS_CORE"
		};
 		units[] = {};
 		weapons[] = {
			#include<WeaponList.hpp>
		};
		magazines[] = {};
		ammo[] = {};
 		requiredVersion = 0.1;
 	};
};

class cfgWeapons
{
	//Externals
	class ItemInfo;
	class UniformItem;
	class VestItem;
	class HeadgearItem;
	class Uniform_Base;
	class HitpointsProtectionInfo;
	
	class OPTRE_UNSC_M52A_Armor1_WDL;
	class OPTRE_UNSC_M52A_Armor2_WDL;
	class OPTRE_UNSC_M52A_Armor3_WDL;
	class OPTRE_UNSC_M52A_Armor4_WDL;
	class OPTRE_UNSC_M52A_Armor_Soft;
	class OPTRE_UNSC_M52A_Armor_SoftD;
	class OPTRE_UNSC_M52A_Armor_SoftDK;
	class OPTRE_UNSC_M52A_Armor_Sniper_WDL;
	class OPTRE_UNSC_M52A_Armor_Rifleman_WDL;
	class OPTRE_UNSC_M52A_Armor_MG_WDL;
	class OPTRE_UNSC_M52A_Armor_Grenadier_WDL;
	class OPTRE_UNSC_M52A_Armor_Marksman_WDL;
	class OPTRE_UNSC_M52A_Armor_Breacher_WDL;
	class OPTRE_UNSC_M52A_Armor_TL_WDL;
	class OPTRE_UNSC_M52A_Armor_Medic_WDL;
	
	class OPTRE_UNSC_M52D_Armor;
	class OPTRE_UNSC_M52D_Armor_Demolitions;
	class OPTRE_UNSC_M52D_Armor_Sniper;
	class OPTRE_UNSC_M52D_Armor_Medic;
	class OPTRE_UNSC_M52D_Armor_Marksman;
	class OPTRE_UNSC_M52D_Armor_Rifleman;
	class OPTRE_UNSC_M52D_Armor_Scout;
	class OPTRE_UNSC_M52D_Armor_Light;
	
	class OPTRE_UNSC_CH252_Helmet_Base;
	class OPTRE_UNSC_CH252A_Helmet_Base;
	class OPTRE_UNSC_CH252_Helmet_Vacuum_WDL;
	class OPTRE_UNSC_CH252_Helmet_WDL;
	class OPTRE_UNSC_CH252_Helmet2_WDL;
	class OPTRE_UNSC_CH252_Helmet2_Vacuum_WDL;
	class OPTRE_UNSC_CH252D_Helmet;
	class OPTRE_UNSC_CH252D_Helmet_dp;
	class OPTRE_Helmet_NavyDeckCrew;

	class OPTRE_UNSC_Army_Uniform_WDL;

	class OPTRE_NVG;
	
	#include<CfgWeapons.hpp>
};

class CfgVehicles
{
	class OPTRE_UNSC_Army_Soldier_WDL;
	#include<CfgVehicles.hpp>
};