-- How many total Characters are there?
SELECT
    COUNT(DISTINCT "name")
FROM
    charactercreator_character
    
-- How many of each specific subclass?
SELECT
    COUNT(DISTINCT m.character_ptr_id) AS MageCount,
    COUNT(DISTINCT t.character_ptr_id) AS ThiefCount,
    COUNT(DISTINCT c.character_ptr_id) AS ClericCount,
    COUNT(DISTINCT f.character_ptr_id) AS FighterCount
FROM
    charactercreator_mage m, 
    charactercreator_thief t,
    charactercreator_cleric c,
    charactercreator_fighter f
    
-- How many total Items?
SELECT
    COUNT(DISTINCT name) AS ItemsCount
FROM
    armory_item

-- How many of the Items are weapons? How many are not?
SELECT
    COUNT(DISTINCT armory_weapon.item_ptr_id) AS TotalWeapons,
    COUNT(DISTINCT armory_item.item_id) - COUNT(DISTINCT armory_weapon.item_ptr_id) AS NotWeapons
FROM
    armory_item,
    armory_weapon

-- How many Items does each character have? (Return first 20 rows)
SELECT
    character_id,
    COUNT(DISTINCT item_id) AS Items_Count
FROM
    charactercreator_character_inventory
GROUP BY
    character_id
LIMIT 20

-- How many Weapons does each character have? (Return first 20 rows)
SELECT
    charactercreator_character_inventory.character_id,
    COUNT(DISTINCT charactercreator_character_inventory.item_id) AS Weapons_Count
FROM
    charactercreator_character_inventory
    LEFT JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
    INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY
    charactercreator_character_inventory.character_id
LIMIT 20

-- On average, how many Items does each Character have?
SELECT
    AVG(Items_Count) AS Average_Items
FROM (
    SELECT
        COUNT(DISTINCT item_id) AS Items_Count
    FROM
        charactercreator_character_inventory
    GROUP BY
        character_id)


-- On average, how many Weapons does each character have?
SELECT
    AVG(Weapons_Count) AS Average_Weapons
FROM (
    SELECT
        COUNT(DISTINCT charactercreator_character_inventory.item_id) AS Weapons_Count
    FROM
        charactercreator_character_inventory
    LEFT JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
    INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY
    charactercreator_character_inventory.character_id)