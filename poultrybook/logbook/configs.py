CNT_BIRDS_NUMBER 	= 'BRD_BIRDS'	# количество птицы в птичнике
CNT_BIRDS_DIED 		= 'BRD_DIED'	# количество умершей птицы (падеж)
CNT_BIRDS_APPEND 	= 'BRD_APPEND' 	# количество добавленой птицы
CNT_BIRDS_REMOVED 	= 'BRD_REMOVED'	# количество изьятой птицы
CNT_BIRDS_WEIGHT 	= 'BRD_WEIGHT'	# средний вес птицы
CNT_BIRDS_UNIF 		= 'BRD_UNIF'	# значение однородности поголовья
CNT_CLIMAT_RTEMP 	= 'CLM_RTEMP'	# средняя температура в помещении
CNT_CLIMAT_RHUM 	= 'CLM_RHUM'	# влажность воздуха в помещении
CNT_CLIMAT_CO2 		= 'CLM_CO2'		# концентрация CO2 в помещении
CNT_CLIMAT_NH3 		= 'CLM_NH3'		# концентрация NH3 в помещении
CNT_SERVICE_INSPECT	= 'SRV_INSPECT'	# осмотр оборудования
CNT_SERVICE_REPAIR	= 'SRV_REPAIR'	# ремонт оборудования
CNT_SERVICE_SETUP	= 'SRV_SETUP'	# настройка оборудования
CNT_SERVICE_REPLACE	= 'SRV_REPLACE'	# замена оборудования
CNT_VET_INSPECT		= 'VET_INSPECT'	# осмотр птицы
CNT_VET_VACCINATION	= 'VET_VACCIN'	# вакцинация птицы
CNT_VET_CURING		= 'VET_CURING'	# лечение птицы


RECORDS_TYPES = {
	CNT_BIRDS_NUMBER 	: 'logbook.IntegerRecord',
	CNT_BIRDS_DIED 		: 'logbook.IntegerRecord',
	CNT_BIRDS_APPEND 	: 'logbook.IntegerRecord',
	CNT_BIRDS_REMOVED 	: 'logbook.IntegerRecord',
	CNT_BIRDS_WEIGHT 	: 'logbook.FloatRecord',
	CNT_BIRDS_UNIF 		: 'logbook.FloatRecord',
	CNT_CLIMAT_RTEMP 	: 'logbook.FloatRecord',
	CNT_CLIMAT_RHUM 	: 'logbook.FloatRecord',
	CNT_CLIMAT_CO2 		: 'logbook.FloatRecord',
	CNT_CLIMAT_NH3 		: 'logbook.FloatRecord',
	CNT_SERVICE_INSPECT	: 'logbook.TextRecord',
	CNT_SERVICE_REPAIR	: 'logbook.TextRecord',
	CNT_SERVICE_SETUP	: 'logbook.TextRecord',
	CNT_SERVICE_REPLACE	: 'logbook.TextRecord',
	CNT_VET_INSPECT		: 'logbook.TextRecord',
	CNT_VET_VACCINATION	: 'logbook.TextRecord',
	CNT_VET_CURING		: 'logbook.TextRecord',
	}


CNT_CHOICES = [
	(CNT_BIRDS_NUMBER, 		'Entered birds number'),
	(CNT_BIRDS_DIED, 		'Entered birds died'),
	(CNT_BIRDS_APPEND, 		'Entered birds append'),
	(CNT_BIRDS_REMOVED, 	'Entered birds removed'),
	(CNT_BIRDS_WEIGHT, 		'Entered birds weight'),
	(CNT_BIRDS_UNIF, 		'Entered birds uniformity'),
	(CNT_CLIMAT_RTEMP, 		'Entered room temperature'),
	(CNT_CLIMAT_RHUM, 		'Entered room humidity'),
	(CNT_CLIMAT_CO2, 		'Entered CO2 concentration'),
	(CNT_CLIMAT_NH3, 		'Entered NH3 concentration'),
	(CNT_SERVICE_INSPECT, 	'Equipent ispection'),
	(CNT_SERVICE_REPAIR, 	'Equipment repair'),
	(CNT_SERVICE_SETUP, 	'Equipment setup'),
	(CNT_SERVICE_REPLACE, 	'Equipment replace'),
	(CNT_VET_INSPECT, 		'Poultry inspection'),
	(CNT_VET_VACCINATION, 	'Poultry vaccination'),
	(CNT_VET_CURING, 		'Poultry curing'),
	]


RECORDS_CONFIG = {
	CNT_BIRDS_NUMBER: {	
		'content_type'	: CNT_BIRDS_NUMBER,
		'title'			: "Поголів'я", 
		'id'			: CNT_BIRDS_NUMBER,
		'color_class'	: 'success', 
		'icon_class'	: 'fas fa-kiwi-bird',
	},
	CNT_BIRDS_DIED: {	
		'content_type'	: CNT_BIRDS_DIED,
		'title'			: 'Падіж', 
		'id'			: CNT_BIRDS_DIED,
		'color_class'	: 'success', 
		'icon_class'	: 'fas fa-skull-crossbones',
	},	
	CNT_BIRDS_APPEND: {	
		'content_type'	: CNT_BIRDS_APPEND,
		'title'			: 'Добавлено', 
		'id'			: CNT_BIRDS_APPEND,
		'color_class'	: 'success', 
		'icon_class'	: 'fas fa-plus-circle',
	},	
	CNT_BIRDS_REMOVED: {
		'content_type'	: CNT_BIRDS_REMOVED,
		'title'			: 'Вилучено', 
		'id'			: CNT_BIRDS_REMOVED,
		'color_class'	: 'success', 
		'icon_class'	: 'fas fa-minus-circle',
	},	
	'BidrsMovedModalForm': {
		'content_type'	: None,
		'title'			: 'Переміщено', 
		'id'			: 'BidrsMovedModalForm', 
		'color_class'	: 'success', 
		'icon_class'	: 'fas fa-arrow-alt-circle-right',
	},	
	CNT_BIRDS_WEIGHT: {
		'content_type'	: CNT_BIRDS_WEIGHT,
		'title'			: 'Вага', 
		'id'			: CNT_BIRDS_WEIGHT,
		'color_class'	: 'success', 
		'icon_class'	: 'fas fa-balance-scale',
	},	
	CNT_BIRDS_UNIF: {
		'content_type'	: CNT_BIRDS_UNIF,
		'title'			: 'Однорідність', 
		'id'			: CNT_BIRDS_UNIF,
		'color_class'	: 'success', 
		'icon_class'	: 'fas fa-feather',
	},		
	CNT_CLIMAT_RTEMP: {
		'content_type'	: CNT_CLIMAT_RTEMP,
		'title'			: 'Температура', 
		'id'			: CNT_CLIMAT_RTEMP, 
		'color_class'	: 'warning', 
		'icon_class'	: 'fas fa-thermometer-three-quarters',
	},
	CNT_CLIMAT_RHUM: {
		'content_type'	: CNT_CLIMAT_RHUM,
		'title'			: 'Вологість', 
		'id'			: CNT_CLIMAT_RHUM,
		'color_class'	: 'warning', 
		'icon_class'	: 'fas fa-tint',
	},	
	CNT_CLIMAT_CO2: {
		'content_type'	: CNT_CLIMAT_CO2,
		'title'			: 'СО2', 
		'id'			: CNT_CLIMAT_CO2,
		'color_class'	: 'warning', 
		'icon_class'	: 'fab fa-cloudscale',
	},	
	CNT_CLIMAT_NH3: {
		'content_type'	: CNT_CLIMAT_NH3,
		'title'			: 'NH3', 
		'id'			: CNT_CLIMAT_NH3,
		'color_class'	: 'warning', 
		'icon_class'	: 'fab fa-cloudscale',
	},		
	CNT_SERVICE_SETUP: {
		'content_type'	: CNT_SERVICE_SETUP,
		'title'			: 'Налаштування', 
		'id'			: CNT_SERVICE_SETUP, 
		'color_class'	: 'dark', 
		'icon_class'	: 'fas fa-cog',
	},
	CNT_SERVICE_INSPECT: {
		'content_type'	: CNT_SERVICE_INSPECT,
		'title'			: 'Огляд', 
		'id'			: CNT_SERVICE_INSPECT, 
		'color_class'	: 'dark', 
		'icon_class'	: 'fas fa-clipboard-check',
	},
	CNT_SERVICE_REPAIR: {
		'content_type'	: CNT_SERVICE_REPAIR,
		'title'			: 'Ремонт', 
		'id'			: CNT_SERVICE_REPAIR, 
		'color_class'	: 'dark', 
		'icon_class'	: 'fas fa-tools',
	},
	CNT_SERVICE_REPLACE: {
		'content_type'	: CNT_SERVICE_REPLACE,
		'title'			: 'Заміна', 
		'id'			: CNT_SERVICE_REPLACE, 
		'color_class'	: 'dark', 
		'icon_class'	: 'fas fa-sync-alt',
	},
	CNT_VET_INSPECT: {
		'content_type'	: CNT_VET_INSPECT,
		'title'			: 'Огляд', 
		'id'			: CNT_VET_INSPECT,
		'color_class'	: 'primary', 
		'icon_class'	: 'fas fa-eye',
	},
	CNT_VET_VACCINATION: {
		'content_type'	: CNT_VET_VACCINATION,
		'title'			: 'Вакцинація', 
		'id'			: CNT_VET_VACCINATION, 
		'color_class'	: 'primary', 
		'icon_class'	: 'fas fa-syringe',
	},
	CNT_VET_CURING: {
		'content_type'	: CNT_VET_CURING,
		'title'			: 'Лікування', 
		'id'			: CNT_VET_CURING,
		'color_class'	: 'primary', 
		'icon_class'	: 'fas fa-briefcase-medical',
	},
}

BIRDS_WORKSPACE_CONFIG = [
	RECORDS_CONFIG[CNT_BIRDS_NUMBER], 
	RECORDS_CONFIG[CNT_BIRDS_DIED], 
	RECORDS_CONFIG[CNT_BIRDS_APPEND], 
	RECORDS_CONFIG[CNT_BIRDS_REMOVED], 
	RECORDS_CONFIG['BidrsMovedModalForm'], 
	RECORDS_CONFIG[CNT_BIRDS_WEIGHT], 
	RECORDS_CONFIG[CNT_BIRDS_UNIF], 
]

CLIMAT_WORKSPACE_CONFIG = [
	RECORDS_CONFIG[CNT_CLIMAT_RTEMP], 
	RECORDS_CONFIG[CNT_CLIMAT_RHUM], 
	RECORDS_CONFIG[CNT_CLIMAT_CO2], 
	RECORDS_CONFIG[CNT_CLIMAT_NH3], 
]

SERVICE_WORKSPACE_CONFIG = [
	RECORDS_CONFIG[CNT_SERVICE_SETUP], 
	RECORDS_CONFIG[CNT_SERVICE_INSPECT], 
	RECORDS_CONFIG[CNT_SERVICE_REPAIR], 
	RECORDS_CONFIG[CNT_SERVICE_REPLACE], 
]

VET_WORKSPACE_CONFIG = [
	RECORDS_CONFIG[CNT_VET_INSPECT], 
	RECORDS_CONFIG[CNT_VET_VACCINATION], 
	RECORDS_CONFIG[CNT_VET_CURING], 
]




