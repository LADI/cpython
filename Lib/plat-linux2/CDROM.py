# Generated by h2py from /usr/include/linux/cdrom.h
CDROMPAUSE = 0x5301
CDROMRESUME = 0x5302
CDROMPLAYMSF = 0x5303
CDROMPLAYTRKIND = 0x5304
CDROMREADTOCHDR = 0x5305
CDROMREADTOCENTRY = 0x5306
CDROMSTOP = 0x5307
CDROMSTART = 0x5308
CDROMEJECT = 0x5309
CDROMVOLCTRL = 0x530a
CDROMSUBCHNL = 0x530b
CDROMREADMODE2 = 0x530c
CDROMREADMODE1 = 0x530d
CDROMREADAUDIO = 0x530e
CDROMEJECT_SW = 0x530f
CDROMMULTISESSION = 0x5310
CDROM_GET_MCN = 0x5311
CDROM_GET_UPC = CDROM_GET_MCN
CDROMRESET = 0x5312
CDROMVOLREAD = 0x5313
CDROMREADRAW = 0x5314
CDROMREADCOOKED = 0x5315
CDROMSEEK = 0x5316
CDROMPLAYBLK = 0x5317
CDROMREADALL = 0x5318
CDROMGETSPINDOWN = 0x531d
CDROMSETSPINDOWN = 0x531e
CDROMCLOSETRAY = 0x5319
CDROM_SET_OPTIONS = 0x5320
CDROM_CLEAR_OPTIONS = 0x5321
CDROM_SELECT_SPEED = 0x5322
CDROM_SELECT_DISC = 0x5323
CDROM_MEDIA_CHANGED = 0x5325
CDROM_DRIVE_STATUS = 0x5326
CDROM_DISC_STATUS = 0x5327
CDROM_CHANGER_NSLOTS = 0x5328
CDROM_LOCKDOOR = 0x5329
CDROM_DEBUG = 0x5330
CDROM_GET_CAPABILITY = 0x5331
CDROMAUDIOBUFSIZ = 0x5382
DVD_READ_STRUCT = 0x5390
DVD_WRITE_STRUCT = 0x5391
DVD_AUTH = 0x5392
CDROM_SEND_PACKET = 0x5393
CDROM_NEXT_WRITABLE = 0x5394
CDROM_LAST_WRITTEN = 0x5395
CDROM_TIMED_MEDIA_CHANGE = 0x5396
CDROM_PACKET_SIZE = 12
CGC_DATA_UNKNOWN = 0
CGC_DATA_WRITE = 1
CGC_DATA_READ = 2
CGC_DATA_NONE = 3
MEDIA_CHANGED_FLAG = 0x1
CD_MINS = 74
CD_SECS = 60
CD_FRAMES = 75
CD_SYNC_SIZE = 12
CD_MSF_OFFSET = 150
CD_CHUNK_SIZE = 24
CD_NUM_OF_CHUNKS = 98
CD_FRAMESIZE_SUB = 96
CD_HEAD_SIZE = 4
CD_SUBHEAD_SIZE = 8
CD_EDC_SIZE = 4
CD_ZERO_SIZE = 8
CD_ECC_SIZE = 276
CD_FRAMESIZE = 2048
CD_FRAMESIZE_RAW = 2352
CD_FRAMESIZE_RAWER = 2646
CD_FRAMESIZE_RAW1 = (CD_FRAMESIZE_RAW-CD_SYNC_SIZE)
CD_FRAMESIZE_RAW0 = (CD_FRAMESIZE_RAW-CD_SYNC_SIZE-CD_HEAD_SIZE)
CD_XA_HEAD = (CD_HEAD_SIZE+CD_SUBHEAD_SIZE)
CD_XA_TAIL = (CD_EDC_SIZE+CD_ECC_SIZE)
CD_XA_SYNC_HEAD = (CD_SYNC_SIZE+CD_XA_HEAD)
CDROM_LBA = 0x01
CDROM_MSF = 0x02
CDROM_DATA_TRACK = 0x04
CDROM_LEADOUT = 0xAA
CDROM_AUDIO_INVALID = 0x00
CDROM_AUDIO_PLAY = 0x11
CDROM_AUDIO_PAUSED = 0x12
CDROM_AUDIO_COMPLETED = 0x13
CDROM_AUDIO_ERROR = 0x14
CDROM_AUDIO_NO_STATUS = 0x15
CDC_CLOSE_TRAY = 0x1
CDC_OPEN_TRAY = 0x2
CDC_LOCK = 0x4
CDC_SELECT_SPEED = 0x8
CDC_SELECT_DISC = 0x10
CDC_MULTI_SESSION = 0x20
CDC_MCN = 0x40
CDC_MEDIA_CHANGED = 0x80
CDC_PLAY_AUDIO = 0x100
CDC_RESET = 0x200
CDC_DRIVE_STATUS = 0x800
CDC_GENERIC_PACKET = 0x1000
CDC_CD_R = 0x2000
CDC_CD_RW = 0x4000
CDC_DVD = 0x8000
CDC_DVD_R = 0x10000
CDC_DVD_RAM = 0x20000
CDC_MO_DRIVE = 0x40000
CDC_MRW = 0x80000
CDC_MRW_W = 0x100000
CDC_RAM = 0x200000
CDS_NO_INFO = 0
CDS_NO_DISC = 1
CDS_TRAY_OPEN = 2
CDS_DRIVE_NOT_READY = 3
CDS_DISC_OK = 4
CDS_AUDIO = 100
CDS_DATA_1 = 101
CDS_DATA_2 = 102
CDS_XA_2_1 = 103
CDS_XA_2_2 = 104
CDS_MIXED = 105
CDO_AUTO_CLOSE = 0x1
CDO_AUTO_EJECT = 0x2
CDO_USE_FFLAGS = 0x4
CDO_LOCK = 0x8
CDO_CHECK_TYPE = 0x10
CD_PART_MAX = 64
CD_PART_MASK = (CD_PART_MAX - 1)
GPCMD_BLANK = 0xa1
GPCMD_CLOSE_TRACK = 0x5b
GPCMD_FLUSH_CACHE = 0x35
GPCMD_FORMAT_UNIT = 0x04
GPCMD_GET_CONFIGURATION = 0x46
GPCMD_GET_EVENT_STATUS_NOTIFICATION = 0x4a
GPCMD_GET_PERFORMANCE = 0xac
GPCMD_INQUIRY = 0x12
GPCMD_LOAD_UNLOAD = 0xa6
GPCMD_MECHANISM_STATUS = 0xbd
GPCMD_MODE_SELECT_10 = 0x55
GPCMD_MODE_SENSE_10 = 0x5a
GPCMD_PAUSE_RESUME = 0x4b
GPCMD_PLAY_AUDIO_10 = 0x45
GPCMD_PLAY_AUDIO_MSF = 0x47
GPCMD_PLAY_AUDIO_TI = 0x48
GPCMD_PLAY_CD = 0xbc
GPCMD_PREVENT_ALLOW_MEDIUM_REMOVAL = 0x1e
GPCMD_READ_10 = 0x28
GPCMD_READ_12 = 0xa8
GPCMD_READ_BUFFER = 0x3c
GPCMD_READ_BUFFER_CAPACITY = 0x5c
GPCMD_READ_CDVD_CAPACITY = 0x25
GPCMD_READ_CD = 0xbe
GPCMD_READ_CD_MSF = 0xb9
GPCMD_READ_DISC_INFO = 0x51
GPCMD_READ_DVD_STRUCTURE = 0xad
GPCMD_READ_FORMAT_CAPACITIES = 0x23
GPCMD_READ_HEADER = 0x44
GPCMD_READ_TRACK_RZONE_INFO = 0x52
GPCMD_READ_SUBCHANNEL = 0x42
GPCMD_READ_TOC_PMA_ATIP = 0x43
GPCMD_REPAIR_RZONE_TRACK = 0x58
GPCMD_REPORT_KEY = 0xa4
GPCMD_REQUEST_SENSE = 0x03
GPCMD_RESERVE_RZONE_TRACK = 0x53
GPCMD_SEND_CUE_SHEET = 0x5d
GPCMD_SCAN = 0xba
GPCMD_SEEK = 0x2b
GPCMD_SEND_DVD_STRUCTURE = 0xbf
GPCMD_SEND_EVENT = 0xa2
GPCMD_SEND_KEY = 0xa3
GPCMD_SEND_OPC = 0x54
GPCMD_SET_READ_AHEAD = 0xa7
GPCMD_SET_STREAMING = 0xb6
GPCMD_START_STOP_UNIT = 0x1b
GPCMD_STOP_PLAY_SCAN = 0x4e
GPCMD_TEST_UNIT_READY = 0x00
GPCMD_VERIFY_10 = 0x2f
GPCMD_WRITE_10 = 0x2a
GPCMD_WRITE_12 = 0xaa
GPCMD_WRITE_AND_VERIFY_10 = 0x2e
GPCMD_WRITE_BUFFER = 0x3b
GPCMD_SET_SPEED = 0xbb
GPCMD_PLAYAUDIO_TI = 0x48
GPCMD_GET_MEDIA_STATUS = 0xda
GPMODE_VENDOR_PAGE = 0x00
GPMODE_R_W_ERROR_PAGE = 0x01
GPMODE_WRITE_PARMS_PAGE = 0x05
GPMODE_WCACHING_PAGE = 0x08
GPMODE_AUDIO_CTL_PAGE = 0x0e
GPMODE_POWER_PAGE = 0x1a
GPMODE_FAULT_FAIL_PAGE = 0x1c
GPMODE_TO_PROTECT_PAGE = 0x1d
GPMODE_CAPABILITIES_PAGE = 0x2a
GPMODE_ALL_PAGES = 0x3f
GPMODE_CDROM_PAGE = 0x0d
DVD_STRUCT_PHYSICAL = 0x00
DVD_STRUCT_COPYRIGHT = 0x01
DVD_STRUCT_DISCKEY = 0x02
DVD_STRUCT_BCA = 0x03
DVD_STRUCT_MANUFACT = 0x04
DVD_LAYERS = 4
DVD_LU_SEND_AGID = 0
DVD_HOST_SEND_CHALLENGE = 1
DVD_LU_SEND_KEY1 = 2
DVD_LU_SEND_CHALLENGE = 3
DVD_HOST_SEND_KEY2 = 4
DVD_AUTH_ESTABLISHED = 5
DVD_AUTH_FAILURE = 6
DVD_LU_SEND_TITLE_KEY = 7
DVD_LU_SEND_ASF = 8
DVD_INVALIDATE_AGID = 9
DVD_LU_SEND_RPC_STATE = 10
DVD_HOST_SEND_RPC_STATE = 11
DVD_CPM_NO_COPYRIGHT = 0
DVD_CPM_COPYRIGHTED = 1
DVD_CP_SEC_NONE = 0
DVD_CP_SEC_EXIST = 1
DVD_CGMS_UNRESTRICTED = 0
DVD_CGMS_SINGLE = 2
DVD_CGMS_RESTRICTED = 3
CDF_RWRT = 0x0020
CDF_HWDM = 0x0024
CDF_MRW = 0x0028
CDM_MRW_NOTMRW = 0
CDM_MRW_BGFORMAT_INACTIVE = 1
CDM_MRW_BGFORMAT_ACTIVE = 2
CDM_MRW_BGFORMAT_COMPLETE = 3
MRW_LBA_DMA = 0
MRW_LBA_GAA = 1
MRW_MODE_PC_PRE1 = 0x2c
MRW_MODE_PC = 0x03
