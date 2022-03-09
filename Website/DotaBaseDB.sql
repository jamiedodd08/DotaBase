DROP DATABASE IF EXISTS DotaBaseDB;

CREATE DATABASE DotaBaseDB;

CREATE TABLE DotaBaseDB.Users (
    UserID int(11) NOT NULL AUTO_INCREMENT,
    Username varchar(45),
    UserPassword varchar(90),
    EmailAddress varchar(40),
    PRIMARY KEY (UserID)
)AUTO_INCREMENT=1;

CREATE TABLE DotaBaseDB.Heroes (
    HeroID int(11) NOT NULL AUTO_INCREMENT,
    HeroName varchar(40),
    HeroIconLink varchar(255),
    HeroAttribute varchar(20),
    HeroRole varchar(15),
    HeroLane1 varchar(15),
    HeroLane2 varchar(15),
    PRIMARY KEY (HeroID)
)AUTO_INCREMENT=1;

CREATE TABLE DotaBaseDB.Abilities (
    AbilityID int (11) NOT NULL AUTO_INCREMENT,
    HeroID int (11),
    AbilityName varchar(30),
    AbilityIconLink varchar(255),
    PRIMARY KEY (AbilityID),
    FOREIGN KEY (HeroID) REFERENCES Heroes(HeroID)
)AUTO_INCREMENT=1;

CREATE TABLE DotaBaseDB.AbilityInfo (
    AbilityInfoID int(11) NOT NULL AUTO_INCREMENT,
    AbilityID int(11),
    UserID int(11),
    AbilityUserInfo TEXT,
    AbilityUpVote int(11),
    AbilityDownVote int(11),
    PRIMARY KEY (AbilityInfoID),
    FOREIGN KEY (AbilityID) REFERENCES Abilities(AbilityID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)AUTO_INCREMENT=1;

CREATE TABLE DotaBaseDB.Counters (
    CounterID int(11) NOT NULL AUTO_INCREMENT,
    HeroID int(11),
    UserID int(11),
    CounterUserInfo TEXT,
    CounterUpVote int(11),
    CounterDownVoter int(11),
    PRIMARY KEY (CounterID),
    FOREIGN KEY (HeroID) REFERENCES Heroes(HeroID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)AUTO_INCREMENT=1;

CREATE TABLE DotaBaseDB.Items (
    ItemID int(11) NOT NULL AUTO_INCREMENT,
    ItemName varchar(30),
    ItemIconLink varchar(255),
    PRIMARY KEY (ItemID)
)AUTO_INCREMENT=1;

CREATE TABLE DotaBaseDB.ItemInfo (
    ItemInfoID int(11) NOT NULL AUTO_INCREMENT,
    ItemID int(11),
    UserID int(11),
    ItemUserInfo TEXT,
    ItemUpVote int(11),
    ItemDownVote int(11),
    PRIMARY KEY (ItemInfoID),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)AUTO_INCREMENT=1;

CREATE TABLE DotaBaseDB.HeroItems (
    HeroItem int(11),
    ItemID int(11),
    HeroItemUserInfo TEXT,
    HeroItemUpVote int(11),
    HeroItemDownVote int(11),
    PRIMARY KEY (HeroItem),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

CREATE TABLE DotaBaseDB.Disscussion (
    LogID int(11) NOT NULL AUTO_INCREMENT,
    HeroID int(11),
    UserID int(11),
    LogText TEXT,
    Upvote int(11),
    DownVote int(11),
    PRIMARY KEY (LogID),
    FOREIGN KEY (HeroID) REFERENCES Heroes(HeroID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
)AUTO_INCREMENT=1;

CREATE TABLE DotaBaseDB.Clips (
    ClipID int(11),
    HeroID int(11),
    UserID int(11),
    ClipUpVote int(11),
    ClipDownVote int(11),
    PRIMARY KEY (ClipID),
    FOREIGN KEY (HeroID) REFERENCES Heroes(HeroID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- INSERT HEROES INTO DATABASE
INSERT INTO DotaBaseDB.Heroes (HeroName, HeroIconLink, HeroAttribute, HeroRole, HeroLane1, HeroLane2)
VALUES
('Abaddon','x','Strength','Core','Off Lane','Safe Lane'),
('Alchemist','x','Strength','Core','Mid Lane','Safe Lane'),
('Ancient Apparition','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Anti-Mage','x','Agility','Core','Safe Lane', ''),
('Arc Warden','x','Agility','Core','Mid Lane', 'Safe Lane'),
('Axe','x','Strength','Core','Off Lane', ''),
('Bane','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Batrider','x','Intelligence','Support','Safe Lane', 'Mid Lane'),
('Beastmaster','x','Strength','Core','Off Lane', ''),
('Bloodseeker','x','Agility','Core','Safe Lane', 'Off Lane'),
('Bounty Hunter','x','Agility','Core','Off Lane', ''),
('Brewmaster','x','Strength','Core','Off Lane', 'Mid Lane'),
('Bristleback','x','Strength','Core','Off Lane', ''),
('Broodmother','x','Agility','Core','Mid Lane', 'Off Lane'),
('Centaur Warrunner','x','Strength','Core','Off Lane', ''),
('Chaos Knight','x','Strength','Core','Safe Lane', 'Off Lane'),
('Chen','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Clinkz','x','Agility','Core','Safe Lane', 'Mid Lane'),
('Clockwerk','x','Strength','Core','Off Lane', 'Safe Lane'),
('Crystal Maiden','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Dark Seer','x','Intelligence','Support','Off Lane', ''),
('Dark Willow','x','Intelligence','Support','Off Lane', 'Safe Lane'),
('Dawnbreaker','x','Strength','Support','Off Lane', ''),
('Dazzle','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Death Prophet','x','Intelligence','Core','Mid Lane', 'Off Lane'),
('Disruptor','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Doom','x','Strength','Core','Off Lane', ''),
('Dragon Knight','x','Strength','Core','Off Lane', 'Mid Lane'),
('Drow Ranger','x','Agility','Core','Safe Lane', 'Mid Lane'),
('Earth Spirit','x','Strength','Support','Off Lane', 'Safe Lane'),
('Earthshaker','x','Strength','Support','Off Lane', 'Safe Lane'),
('Elder Titan','x','Strength','Support','Off Lane', 'Safe Lane'),
('Ember Spirit','x','Agility','Core','Mid Lane', 'Safe Lane'),
('Enchantress','x','Intelligence','Support','Off Lane', 'Safe Lane'),
('Enigma','x','Intelligence','Core','Off Lane', ''),
('Faceless Void','x','Agility','Core','Safe Lane', 'Off Lane'),
('Grimstroke','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Gyrocopter','x','Agility','Core','Safe Lane', 'Off Lane'),
('Hoodwink','x','Agility','Support','Off Lane', 'Safe Lane'),
('Huskar','x','Strength','Core','Mid Lane', 'Safe Lane'),
('Invoker','x','Intelligence','Core','Mid Lane', ''),
('Io','x','Strength','Support','Safe Lane', 'Off Lane'),
('Jakiro','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Juggernaut','x','Agility','Core','Safe Lane', ''),
('Keeper of the Light','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Kunkka','x','Strength','Core','Mid Lane', 'Safe Lane'),
('Legion Commander','x','Strength','Core','Off Lane', 'Safe Lane'),
('Leshrac','x','Intelligence','Core','Mid Lane', 'Off Lane'),
('Lich','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Lifestealer','x','Strength','Core','Safe Lane', ''),
('Lina','x','Intelligence','Core','Mid Lane', 'Off Lane'),
('Lion','x','Intelligence','Support','Safe Lane', 'Off Lane'),
('Lone Druid','x','Agility','Core','Off Lane', 'Safe Lane'),
('Luna','x','Agility','Core','Safe Lane', 'Off Lane'),
('Lycan','x','Strength','Core','Safe Lane', 'Off Lane'),
('Magnus','x','Strength','Support','Off Lane', 'Mid Lane'),
('Marci','x','Strength','Core','Off Lane', 'Safe Lane'),
('Mars','x','Strength','Core','Off Lane', ''),
('Medusa','x','Agility','Core','Safe Lane', 'Mid Lane'),
('Meepo','x','Agility','Core','Mid Lane', ''),
('Mirana','x','Agility','Support','Off Lane', 'Mid Lane'),
('Monkey King','x','Agility','Core','Safe Lane', 'Mid Lane'),
('Morphling','x','Agility','Core','Safe Lane', 'Mid Lane'),
('Naga Siren','x','Agility','Core','Safe Lane', ''),
("Nature's Prophet",'x','Intelligence','Core','Off Lane', ''),
('Necrophos','x','Intelligence','Core','Off Lane', 'Mid Lane'),
('Night Stalker','x','Strength','Core','Off Lane', ''),
('Nyx Assassin','x','Agility','Support','Off Lane', 'Safe Lane'),
('Ogre Magi','x','Strength','Support','Safe Lane', 'Off Lane'),
('Omniknight','x','Strength','Support','Safe Lane', 'Off Lane'),
('Oracle','x','Intelligence','Support','Safe Lane', ''),
('Outworld Destroyer','x','Intelligence','Core','Mid Lane', ''),
('Pangolier','x','Agility','Core','Off Lane', ''),
('Phantom Assassin','x','Agility','Core','Safe Lane','Mid Lane'),
('Phantom Lancer','x','Agility','Core','Safe Lane', ''),
('Phoenix','x','Strength','Support','Off Lane','Safe Lane'),
('Primal Beast','x','Strength','Support','Off Lane','Safe Lane'),
('Puck','x','Intelligence','Core','Mid Lane','Off Lane'),
('Pudge','x','Strength','Core','Off Lane','Mid Lane'),
('Pugna','x','Intelligence','Support','Off Lane','Mid Lane'),
('Queen of Pain','x','Intelligence','Core','Mid Lane',''),
('Razor','x','Agility','Core','Mid Lane','Off Lane'),
('Riki','x','Agility','Core','Off Lane','Safe Lane'),
('Rubick','x','Intelligence','Support','Safe Lane','Off Lane'),
('Sand King','x','Strength','Core','Off Lane',''),
('Shadow Demon','x','Intelligence','Support','Safe Lane','Off Lane'),
('Shadow Fiend','x','Agility','Core','Mid Lane',''),
('Shadow Shaman','x','Intelligence','Support','Safe Lane','Off Lane'),
('Silencer','x','Intelligence','Support','Safe Lane','Off Lane'),
('Skywrath Mage','x','Intelligence','Support','Off Lane','Safe Lane'),
('Slardar','x','Strength','Core','Off Lane','Safe Lane'),
('Slark','x','Agility','Core','Safe Lane',''),
('Snapfire','x','Strength','Support','Off Lane','Safe Lane'),
('Sniper','x','Agility','Core','Mid Lane','Safe Lane'),
('Spectre','x','Agility','Core','Safe Lane',''),
('Spirit Breaker','x','Strength','Core','Off Lane',''),
('Storm Spirit','x','Intelligence','Core','Mid Lane',''),
('Sven','x','Strength','Core','Safe Lane',''),
('Techies','x','Intelligence','Support','Off Lane',''),
('Templar Assassin','x','Agility','Core','Mid Lane',''),
('Terrorblade','x','Agility','Core','Safe Lane',''),
('Tidehunter','x','Strength','Core','Off Lane',''),
('Timbersaw','x','Strength','Core','Off Lane',''),
('Tinker','x','Intelligence','Core','Mid Lane',''),
('Tiny','x','Strength','Core','Off Lane','Mid Lane'),
('Treant Protector','x','Strength','Support','Safe Lane','Off Lane'),
('Troll Warlord','x','Agility','Core','Safe Lane',''),
('Tusk','x','Strength','Core','Off Lane','Safe Lane'),
('Underlord','x','Strength','Core','Off Lane',''),
('Undying','x','Strength','Support','Off Lane','Safe Lane'),
('Ursa','x','Agility','Core','Safe Lane',''),
('Vengeful Spirit','x','Agility','Support','Safe Lane','Off Lane'),
('Venomancer','x','Agility','Support','Off Lane','Safe Lane'),
('Viper','x','Agility','Core','Mid Lane','Off Lane'),
('Visage','x','Intelligence','Core','Mid Lane','Safe Lane'),
('Void Spirit','x','Intelligence','Core','Mid Lane','Off Lane'),
('Warlock','x','Intelligence','Support','Safe Lane','Off Lane'),
('Weaver','x','Agility','Core','Off Lane','Safe Lane'),
('Windranger','x','Intelligence','Core','Off Lane','Mid Lane'),
('Winter Wyvern','x','Intelligence','Support','Safe Lane','Off Lane'),
('Witch Doctor','x','Intelligence','Support','Safe Lane','Off Lane'),
('Wraith King','x','Strength','Core','Safe Lane','Off Lane'),
('Zeus','x','Intelligence','Core','Mid Lane','Off Lane');

-- INSERT ITEMS INTO DATABASE
INSERT INTO DotaBaseDB.Items (ItemName, ItemIconLink)
VALUES
('Abysal Blade','x'),
('Agies of the Immortal','x'),
('Aeon Disk','x'),
('Aether Lens','x'),
("Aghanim's Scepter",'x'),
("Aghanim's Shard",'x'),
('Apex','x'),
('Arcane Blink','x'),
('Arcane Boots','x'),
('Arcane Ring','x'),
("Arcanist's Armor",'x'),
('Armelt of Mordiggian','x'),
("Ascetic's Cap",'x'),
('Assult Cuirass','x'),
('Ballista','x'),
('Band of Elvenskin','x'),
('Battle Fury','x'),
('Belt of Strength','x'),
('Black King Bar','x'),
('Blade Mail','x'),
('Blade of Alacrity','x'),
('Blades of Attack','x'),
('Blast Rig','x'),
('Blight Stone','x'),
('Blink Dagger','x'),
('Blitz Knuckles','x'),
('Bloodstone','x'),
('Bloodthorn','x'),
('Book of Shadows','x'),
('Book of the Dead','x'),
('Boots of Bearing','x'),
('Boots of Speed','x'),
('Boots of Travel','x'),
('Boots of Travel 2','x'),
('Bottle','x'),
('Bracer','x'),
("Brigand's Blade",'x'),
('Broadsword','x'),
('Broom Handle','x'),
('Buckler','x'),
('Bullwhip','x'),
('Butterfly','x'),
('Ceremonial Robe','x'),
('Chainmail','x'),
('Chipped Vest','x'),
('Circlet','x'),
('Claymore','x'),
('Cloak','x'),
('Cloak of Flames','x'),
('Clumsy Net','x'),
('Craggy Coat','x'),
('Crimson Guard','x'),
('Crown','x'),
('Crystalys','x'),
('Daedalus','x'),
('Dagon 1','x'),
('Dagon 2','x'),
('Dagon 3','x'),
('Dagon 4','x'),
('Dagon 5','x'),
('Demon Edge','x'),
('Desolator','x'),
('Desolator 2','x'),
('Diffusal Blade','x'),
('Divine Rapier','x'),
('Dragon Lance','x'),
('Drum of Endurance','x'),
('Dust of Appearance','x'),
('Eaglesong','x'),
('Echo Sabre','x'),
('Elven Tunic','x'),
('Enchanted Quiver','x'),
('Energy Booster','x'),
('Essence Ring','x'),
('Eternal Shroud','x'),
('Etheral Blade','x'),
("Eul's Scepter of Divinity",'x'),
('Ex Machina','x'),
('Eye of Skadi','x'),
('Fae Grenade','x'),
("Fairy's Trinket",'x'),
('Falcon Blade','x'),
('Fallen Sky','x'),
('Flicker','x'),
('Fluffy Hat','x'),
('Force Boots','x'),
('Force Staff','x'),
('Gauntlets of Strength','x'),
('Gem of True Sight','x'),
('Ghost Scepter','x'),
("Giant's Ring",'x'),
('Glepnir','x'),
('Glimmer Cape','x'),
('Gloves of Haste','x'),
('Grove Bow','x'),
('Guardian Greaves','x'),
('Hand of Midas','x'),
('Headdress','x'),
('Heart of Tarrasque','x'),
("Heaven's Halberd",'x'),
('Helm of Iron Will','x'),
('Helm of the Dominator','x'),
('Helm of the Overlord','x'),
('Holy Locket','x'),
('Hood of Defiance','x'),
('Hurricane Pike','x'),
('Hyperstone','x'),
('Infused Raindrops','x'),
('Iron Branch','x'),
('Javelin','x'),
('Kaya','x'),
('Kaya and Sange','x'),
('Keen Optic','x'),
("Linken's Sphere",'x'),
('Lotus Orb','x'),
('Maelstrom','x'),
('Mage Slayer','x'),
('Magic Stick','x'),
('Magic Wand','x'),
('Manta Style','x'),
('Mantle of Intelligence','x'),
('Mask of Madness','x'),
('Medallion of Courage','x'),
('Mekansm','x'),
('Meteor Hammer','x'),
('Mind Breaker','x'),
('Mirror Shield','x'),
('Mithril Hammer','x'),
('Mjollnir','x'),
('Monkey King Bar','x'),
('Moon Shard','x'),
('Morbid Mask','x'),
('Mystic Staff','x'),
('Nether Shawl','x'),
('Ninja Gear','x'),
('Null Talisman','x'),
('Nullifier','x'),
('Oblivion Staff','x'),
('Observer Ward','x'),
('Ocean Heart','x'),
('Octarine Core','x'),
('Ogre Axe','x'),
('Orb of Corrosion','x'),
('Orb of Venom','x'),
('Orchid Malevolence','x'),
('Overwhelming Blink','x'),
('Paladin Sword','x'),
('Penta-Edged Sword','x'),
('Perseverance','x'),
('Phase Boots','x'),
("Philosopher's Stone",'x'),
('Pig Pole','x'),
('Pipe of Insight','x'),
('Pirate Hat','x'),
('Platemail','x'),
('Point Booster','x'),
('Possessed Mask','x'),
('Power Treads','x'),
('Psychic Headband','x'),
("Pupil's Gift",'x'),
('Quarterstaff','x'),
('Quelling Blade','x'),
('Quickening Charm','x'),
('Quicksilver Amulet','x'),
('Radiance','x'),
('Reaver','x'),
('Refresher Orb','x'),
('Refresher Shard','x'),
("Revenant's Brooch",'x'),
('Ring of Aquila','x'),
('Ring of Basilius','x'),
('Ring of Health','x'),
('Ring of Protection','x'),
('Ring of Regen','x'),
('Robe of the Magi','x'),
('Rod of Atos','x'),
('Sacred Relic','x'),
("Sage's Mask",'x'),
('Sange','x'),
('Sange and Yasha','x'),
('Satanic','x'),
('Scythe of Vyse','x'),
('Seer Stone','x'),
('Sentry Ward','x'),
('Shadow Amulet','x'),
('Shadow Blade','x'),
("Shiva's Guard",'x'),
('Silver Edge','x'),
('Skull Basher','x'),
('Slippers of Agility','x'),
('Smoke of Deceit','x'),
('Solar Crest','x'),
('Soul Booster','x'),
('Soul Ring','x'),
('Spell Prism','x'),
('Spider Legs','x'),
('Spirit Vessel','x'),
('Staff of Wizardry','x'),
('Stormcaller','x'),
('Swift Blink','x'),
('Talisman of Evasion','x'),
('Tango','x'),
('Telescope','x'),
('The Leveller','x'),
('Timeless Relic','x'),
('Titan Silver','x'),
('Tome of Knowledge','x'),
('Town Portal Scroll','x'),
('Tranquil Boots','x'),
('Trickster Cloak','x'),
('Trusty Shovel','x'),
("Tumbler's Toy",'x'),
('Ultimate Orb','x'),
('Urn of Shadows','x'),
('Vambrace','x'),
('Vanguard','x'),
('Veil of Discord','x'),
('Vitality Booster','x'),
("Vladmir's Offering",'x'),
('Void Stone','x'),
('Voodoo Mask','x'),
('Wind Lace','x'),
('Wind Waker','x'),
('Witch Blade','x'),
('Witchbane','x'),
('Wraith Band','x'),
('Wraith Pact','x'),
('Yasha','x'),
('Yasha and Kaya','x');

-- INSERT ITEMS INTO DATABASE
INSERT INTO DotaBaseDB.Abilities (HeroID, AbilityName, AbilityIconLink)
VALUES
('1','Mist Coil','x'),
('1','Aphotic Shield','x'),
('1','Curse of Avernus','x'),
('1','Borrowed Time','x'),
('1','Curse of Avernus - Shard Ability Upgrade','x'),
('1','Borrowed Time - Scepter Ability Upgrade','x'),
('2','Acid Spray','x'),
('2','Unstable Concoction','x'),
('2',"Greevil's Greed",'x'),
('2','Chemical Rage','x'),
('2','Berserk Potion','x'),
('2','Chemical Rage - Scepter Ability Upgrade','x'),
('3','Cold Feet','x'),
('3','Ice Vortex','x'),
('3','Chilling Touch','x'),
('3','Ice Blast','x'),
('3','Ice Vortex - Shard Ability Upgrade','x'),
('3','Chilling Touch - Scepter Ability Upgrade','x'),
('4','Mana Break','x'),
('4','Blink','x'),
('4','Counterspell','x'),
('4','Mana Void','x'),
('4','Counterspell - Shard Ability Upgrade','x'),
('4','Blink Fragment','x'),
('5','Flux','x'),
('5','Magnetic Field','x'),
('5','Spark Wraith','x'),
('5','Tempest Double','x'),
('5','Magnetic Field - Shard Ability Upgrade','x'),
('5','Spark Wraith - Scepter Ability Upgrade','x'),
('6',"Berserker's Call",'x'),
('6','Battle Hunger','x'),
('6','Counter Helix','x'),
('6','Culling Blade','x'),
('6','Counter Helix - Shard Ability Upgrade','x'),
('6',"Berserker's Call - Scepter Ability Upgrade",'x'),
('7','Enfeeble','x'),
('7','Brain Sap','x'),
('7','Nightmare','x'),
('7',"Fiend's Grip",'x'),
('7','Brain Sap - Shard Ability Upgrade','x'),
('7',"Fiend's Grip - Scepter Ability Upgrade",'x'),
('8','Sticky Napalm','x'),
('8','Flamebreak','x'),
('8','Firefly','x'),
('8','Flaming Lasso','x'),
('8','Sticky Napalm - Shard Ability Upgrade','x'),
('8','Flaming Lasso - Scepter Ability Upgrade','x'),
('9','Wild Axes','x'),
('9','Call of the Wild Board','x'),
('9','Call of the Wild Hawk','x'),
('9','Inner Beast','x'),
('9','Primal Roar','x'),
('9','Call of the Wild Hawk - Shard Ability Upgrade','x'),
('9','Wild Axes - Scepter Ability Upgrade','x'),
('10','Bloodrage','x'),
('10','Bloodrite','x'),
('10','Thirst','x'),
('10','Rupture','x'),
('10','Bloodrage - Shard Ability Upgrade','x'),
('10','Blood Mist','x'),
('11','Shuriken Toss','x'),
('11','Jinada','x'),
('11','Shadow Walk','x'),
('11','Track','x'),
('11','Shadow Walk - Shard Ability Upgrade','x'),
('11','Shuriken Toss - Scepter Ability Upgrade','x'),
('12','Thunder Clap','x'),
('12','Cinder Brew','x'),
('12','Drunken Brawler','x'),
('12','Primal Split','x'),
('12','Primal Split - Shard Ability Upgrade','x'),
('12','Primal Split - Shard Ability Upgrade','x'),
('13','Viscous Nasal Goo','x'),
('13','Quill Spray','x'),
('13','Bristleback','x'),
('13','Warpath','x'),
('13','Hairball','x'),
('13','Viscous Nasal Goo - Scepter Ability Upgrade','x'),
('14','Insatiable Hunger','x'),
('14','Spin Web','x'),
('14','Silken Bola','x'),
('14','Spawn Spiderlings','x'),
('14','Silken Bola - Shard Ability Upgrade','x'),
('14',"Spinner's Snare",'x'),
('15','Hoof Stomp','x'),
('15','Double Edge','x'),
('15','Retaliate','x'),
('15','Stampede','x'),
('15','Double Edge - Shard Ability Upgrade','x'),
('15','Stampede - Scepter Ability Upgrade','x'),
('15','Chaos Bolt','x'),
('15','Reality Rift','x'),
('15','Chaos Strike','x'),
('15','Phantasm','x'),
('15','Chaos Bolt - Shard Ability Upgrade','x'),
('15','Phantasm - Scepter Ability Upgrade','x');#

INSERT INTO DotaBaseDB.Users (Username, UserPassword)
VALUES
('test', 'test');

INSERT INTO DotaBaseDB.Counters (HeroID, UserID, CounterUserInfo)
VALUES
('2', '1', 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.');