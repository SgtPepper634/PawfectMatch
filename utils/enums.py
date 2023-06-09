from enum import Enum

class UserTypes(Enum):
    ORGANIZATION_EMPLOYEE = 'Organization Employee'
    ADOPTER_FOSTER = 'Adopter/Fosterer'
    GUARDIAN = 'Guardian'

class CarePreferences(Enum):
    FOSTERING = 'Fostering'
    ADOPTING = 'Adopting'

class PetSpecies(Enum):
    DOG = 'Dog'
    CAT = 'Cat'

class DogBreeds(Enum):
    LABRADOR_RETRIEVER = 'Labrador Retriever'
    GERMAN_SHEPHERD = 'German Shepherd'
    GOLDEN_RETRIEVER = 'Golden Retriever'
    FRENCH_BULLDOG = 'French Bulldog'
    BEAGLE = 'Beagle'
    BULLDOG = 'Bulldog'
    POODLE = 'Poodle'
    ROTTWEILER = 'Rottweiler'
    YORKSHIRE_TERRIER = 'Yorkshire Terrier'
    BOXER = 'Boxer'
    SIBERIAN_HUSKY = 'Siberian Husky'
    DACHSHUND = 'Dachshund'
    SHIH_TZU = 'Shih Tzu'
    GREAT_DANE = 'Great Dane'
    CHIHUAHUA = 'Chihuahua'
    BOSTON_TERRIER = 'Boston Terrier'
    POMERANIAN = 'Pomeranian'
    DOBERMAN_PINSCHER = 'Doberman Pinscher'
    SHETLAND_SHEEPDOG = 'Shetland Sheepdog'
    BICHON_FRISE = 'Bichon Frise'
    BORDER_COLLIE = 'Border Collie'
    PITBULL = 'Pitbull'
    CAVALIER_KING_CHARLES_SPANIEL = 'Cavalier King Charles Spaniel'
    AUSTRALIAN_SHEPHERD = 'Australian Shepherd'
    SHAR_PEI = 'Shar Pei'
    JACK_RUSSELL_TERRIER = 'Jack Russell Terrier'
    ALASKAN_MALAMUTE = 'Alaskan Malamute'
    BLOODHOUND = 'Bloodhound'
    WEST_HIGHLAND_WHITE_TERRIER = 'West Highland White Terrier'
    BASSET_HOUND = 'Basset Hound'
    STAFFORDSHIRE_BULL_TERRIER = 'Staffordshire Bull Terrier'
    WEIMARANER = 'Weimaraner'
    SHIBA_INU = 'Shiba Inu'
    BORZOI = 'Borzoi'
    WHIPPET = 'Whippet'
    MALTESE = 'Maltese'
    AKITA = 'Akita'
    CAVOODLE = 'Cavoodle'
    CHOW_CHOW = 'Chow Chow'
    PUG = 'Pug'
    PAPILLON = 'Papillon'
    SAMOYED = 'Samoyed'
    LHASA_APSO = 'Lhasa Apso'
    GREYHOUND = 'Greyhound'
    OLD_ENGLISH_SHEEPDOG = 'Old English Sheepdog'
    IRISH_SETTER = 'Irish Setter'
    NEWFOUNDLAND = 'Newfoundland'
    MINIATURE_SCHNAUZER = 'Miniature Schnauzer'
    AFGHAN_HOUND = 'Afghan Hound'
    CHINESE_CRESTED = 'Chinese Crested'
    IRISH_WOLFHOUND = 'Irish Wolfhound'

# class DogTemperaments(Enum):
#     FRIENDLY = 'Friendly'
#     CONFIDENT = 'Confident'
#     COURAGEOUS = 'Courageous'
#     AFFECTIONATE = 'Affectionate'
#     INDEPENDENT = 'Independent'
#     INTELLIGENT = 'Intelligent'
#     LOYAL = 'Loyal'
#     ALERT = 'Alert'
#     BRAVE = 'Brave'
#     DOCILE = 'Docile'
#     ENERGETIC = 'Energetic'
#     GENTLE = 'Gentle'
#     KIND = 'Kind'
#     PATIENT = 'Patient'
#     PLAYFUL = 'Playful'
#     PROTECTIVE = 'Protective'
#     RESPONSIBLE = 'Responsible'
#     SOCIAL = 'Social'
#     TRAINABLE = 'Trainable'
#     RESERVED = 'Reserved'

class DogCharacteristics(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    GIANT = 'Giant'
    SHORT_HAIRED = 'Short-haired'
    LONG_HAIRED = 'Long-haired'
    DOUBLE_COATED = 'Double-coated'
    SINGLE_COATED = 'Single-coated'
    CURLY = 'Curly'
    STRAIGHT = 'Straight'
    WIRE_HAIRED = 'Wire-haired'
    SMOOTH = 'Smooth'
    BLACK = 'Black'
    WHITE = 'White'
    BROWN = 'Brown'
    GOLDEN = 'Golden'
    BRINDLE = 'Brindle'
    SPOTTED = 'Spotted'
    STRIPED = 'Striped'
    SOLID = 'Solid'
    PIED = 'Pied'
    BLUE_EYES = 'Blue eyes'
    BROWN_EYES = 'Brown eyes'
    HAZEL_EYES = 'Hazel eyes'
    GREEN_EYES = 'Green eyes'
    BLACK_EYES = 'Black eyes'

class PetTemperaments(Enum):
    FRIENDLY = 'Friendly'
    AFFECTIONATE = 'Affectionate'
    PLAYFUL = 'Playful'
    INDEPENDENT = 'Independent'
    LAID_BACK = 'Laid-back'
    GENTLE = 'Gentle'
    SHY = 'Shy'
    RESERVED = 'Reserved'
    VOCAL = 'Vocal'
    ACTIVE = 'Active'
    DOCILE = 'Docile'
    ADAPTABLE = 'Adaptable'
    ATTENTIVE = 'Attentive'
    EASY_GOING = 'Easy-going'
    STUBBORN = 'Stubborn'
    AGGRESSIVE = 'Aggressive'
    ANXIOUS = 'Anxious'
    BRAVE = 'Brave'
    CALM = 'Calm'
    CONFIDENT = 'Confident'
    COURAGEOUS = 'Courageous'
    CURIOUS = 'Curious'
    DEPENDABLE = 'Dependable'
    DEVOTED = 'Devoted'
    EAGER = 'Eager'
    ENERGETIC = 'Energetic'
    FAITHFUL = 'Faithful'
    FEARLESS = 'Fearless'
    FIERCE = 'Fierce'
    GREGARIOUS = 'Gregarious'
    HAPPY = 'Happy'
    HARDWORKING = 'Hardworking'
    HYPER = 'Hyper'
    INTELLIGENT = 'Intelligent'
    JOYFUL = 'Joyful'
    KIND = 'Kind'
    LIVELY = 'Lively'
    LOYAL = 'Loyal'
    MISCHIEVOUS = 'Mischievous'
    NOBLE = 'Noble'
    OBEDIENT = 'Obedient'
    PATIENT = 'Patient'
    PROTECTIVE = 'Protective'
    QUICK = 'Quick'
    QUIET = 'Quiet'
    RELAXED = 'Relaxed'
    RESPONSIBLE = 'Responsible'
    SENSITIVE = 'Sensitive'
    SENSIBLE = 'Sensible'
    SERIOUS = 'Serious'
    SINCERE = 'Sincere'
    SOCIAL = 'Social'
    STOIC = 'Stoic'
    STRONG = 'Strong'
    SWEET = 'Sweet'
    TENACIOUS = 'Tenacious'
    TERRITORIAL = 'Territorial'
    TOUGH = 'Tough'
    TRAINABLE = 'Trainable'
    TRUSTWORTHY = 'Trustworthy'
    VALIANT = 'Valiant'
    VERSATILE = 'Versatile'
    VIGILANT = 'Vigilant'
    ZEALOUS = 'Zealous'

class CatBreeds(Enum):
    AMERICAN_SHORTHAIR = 'American Shorthair'
    PERSIAN = 'Persian'
    SIAMESE = 'Siamese'
    BRITISH_SHORTHAIR = 'British Shorthair'
    BENGAL = 'Bengal'
    MAINE_COON = 'Maine Coon'
    SCOTTISH_FOLD = 'Scottish Fold'
    SPHYNX = 'Sphynx'
    RAGDOLL = 'Ragdoll'
    MANX = 'Manx'
    HIMALAYAN = 'Himalayan'
    BIRMAN = 'Birman'
    ABYSSINIAN = 'Abyssinian'
    DEVON_REX = 'Devon Rex'
    NORWEGIAN_FOREST_CAT = 'Norwegian Forest Cat'
    EXOTIC_SHORTHAIR = 'Exotic Shorthair'
    BALINESE = 'Balinese'
    PETERBALD = 'Peterbald'
    CORNISH_REX = 'Cornish Rex'
    JAPANESE_BOBTAIL = 'Japanese Bobtail'
    TURKISH_ANGORA = 'Turkish Angora'
    TONKINESE = 'Tonkinese'
    AMERICAN_BOBTAIL = 'American Bobtail'
    ORIENTAL_SHORTHAIR = 'Oriental Shorthair'
    SAVANNAH_CAT = 'Savannah Cat'
    SCOTTISH_STRAIGHT = 'Scottish Straight'
    AMERICAN_WIREHAIR = 'American Wirehair'
    BRITISH_LONGHAIR = 'British Longhair'
    CYMRIC = 'Cymric'
    EGYPTIAN_MAU = 'Egyptian Mau'
    KORAT = 'Korat'
    LAPOERM = 'LaPerm'
    OCICAT = 'Ocicat'
    PIXIE_BOB = 'Pixie-Bob'
    SNOWSHOE = 'Snowshoe'
    SOMALI = 'Somali'
    SPHYNX_CAT = 'Sphynx Cat'
    THAI_CAT = 'Thai Cat'
    TURKISH_VAN = 'Turkish Van'

class CatCharacteristics(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    SHORT_HAIRED = 'Short-haired'
    LONG_HAIRED = 'Long-haired'
    DOUBLE_COATED = 'Double-coated'
    SINGLE_COATED = 'Single-coated'
    CURLY = 'Curly'
    STRAIGHT = 'Straight'
    BLACK = 'Black'
    WHITE = 'White'
    GREY = 'Grey'
    BROWN = 'Brown'
    ORANGE = 'Orange'
    CALICO = 'Calico'
    TORTOISESHELL = 'Tortoiseshell'
    TABBY = 'Tabby'
    SIAMESE = 'Siamese'
    PERSIAN = 'Persian'
    BENGAL = 'Bengal'
    RAGDOLL = 'Ragdoll'
    SPHYNX = 'Sphynx'

# class CatTemperaments(Enum):
    FRIENDLY = 'Friendly'
    AFFECTIONATE = 'Affectionate'
    PLAYFUL = 'Playful'
    INDEPENDENT = 'Independent'
    LAID_BACK = 'Laid-back'
    CURIOUS = 'Curious'
    GENTLE = 'Gentle'
    SHY = 'Shy'
    RESERVED = 'Reserved'
    VOCAL = 'Vocal'
    ACTIVE = 'Active'
    DOCILE = 'Docile'
    ADAPTABLE = 'Adaptable'
    ATTENTIVE = 'Attentive'
    EASY_GOING = 'Easy-going'
    PET_FRIENDLY = 'Pet Friendly'