# grafana.ini — Line‑by‑Line Explanation

This is an annotated, line‑by‑line view of the current `grafana.ini`.

Legend:
- **Comment**: line starts with `;` or `#`
- **Section**: `[section]` header
- **Setting**: `key = value`

---

**L0001** `##################### Grafana Configuration Example #####################`

- Comment / default documentation.

**L0002** `#`

- Comment / default documentation.

**L0003** `# Everything has defaults so you only need to uncomment things you want to`

- Comment / default documentation.

**L0004** `# change`

- Comment / default documentation.

**L0005** ``

- Blank line.

**L0006** `# possible values : production, development`

- Comment / default documentation.

**L0007** `;app_mode = production`

- Comment / default documentation.

**L0008** ``

- Blank line.

**L0009** `# instance name, defaults to HOSTNAME environment variable value or hostname if HOSTNAME var is empty`

- Comment / default documentation.

**L0010** `instance_name = Anish Laptop Observability`

- Human‑readable instance name shown in UI.

**L0011** ``

- Blank line.

**L0012** `#################################### Paths ####################################`

- Comment / default documentation.

**L0013** `[paths]`

- Section header: paths

**L0014** `# Path to where grafana can store temp files, sessions, and the sqlite3 db (if that is used)`

- Comment / default documentation.

**L0015** `;data = /var/lib/grafana`

- Comment / default documentation.

**L0016** ``

- Blank line.

**L0017** `# Temporary files in \`data\` directory older than given duration will be removed`

- Comment / default documentation.

**L0018** `;temp_data_lifetime = 24h`

- Comment / default documentation.

**L0019** ``

- Blank line.

**L0020** `# Directory where grafana can store logs`

- Comment / default documentation.

**L0021** `;logs = /var/log/grafana`

- Comment / default documentation.

**L0022** ``

- Blank line.

**L0023** `# Directory where grafana will automatically scan and look for plugins`

- Comment / default documentation.

**L0024** `;plugins = /var/lib/grafana/plugins`

- Comment / default documentation.

**L0025** ``

- Blank line.

**L0026** `# folder that contains provisioning config files that grafana will apply on startup and while running.`

- Comment / default documentation.

**L0027** `;provisioning = conf/provisioning`

- Comment / default documentation.

**L0028** ``

- Blank line.

**L0029** `# Directories that are permitted to contain local repositories.`

- Comment / default documentation.

**L0030** `# This is a list. Each entry is delimited by a pipe (|). No leading or trailing spaces are supported.`

- Comment / default documentation.

**L0031** `# These do not need to be absolute paths, in which case they'll be relative to the path where you are running Grafana.`

- Comment / default documentation.

**L0032** `# Empty entries will return an error, unless the string is just a single pipe.`

- Comment / default documentation.

**L0033** `# Example: permitted_provisioning_paths = /tmp|/etc/grafana/repositories|conf/provisioning`

- Comment / default documentation.

**L0034** `;permitted_provisioning_paths = devenv/dev-dashboards|conf/provisioning`

- Comment / default documentation.

**L0035** ``

- Blank line.

**L0036** `#################################### Server ####################################`

- Comment / default documentation.

**L0037** `[server]`

- Section header: server

**L0038** `# Protocol (http, https, h2, socket)`

- Comment / default documentation.

**L0039** `protocol = https`

- HTTP or HTTPS protocol for the server.

**L0040** ``

- Blank line.

**L0041** `# Minimum TLS version allowed. By default, this value is empty. Accepted values are: TLS1.2, TLS1.3. If nothing is set TLS1.2 would be taken`

- Comment / default documentation.

**L0042** `;min_tls_version = ""`

- Comment / default documentation.

**L0043** ``

- Blank line.

**L0044** `# The ip address to bind to, empty will bind to all interfaces`

- Comment / default documentation.

**L0045** `;http_addr =`

- Comment / default documentation.

**L0046** ``

- Blank line.

**L0047** `# The http port to use`

- Comment / default documentation.

**L0048** `http_port = 3000`

- Port Grafana listens on.

**L0049** ``

- Blank line.

**L0050** `# The public facing domain name used to access grafana from a browser`

- Comment / default documentation.

**L0051** `domain = localhost`

- Domain used to build external URLs.

**L0052** ``

- Blank line.

**L0053** `# Redirect to correct domain if host header does not match domain`

- Comment / default documentation.

**L0054** `# Prevents DNS rebinding attacks`

- Comment / default documentation.

**L0055** `;enforce_domain = false`

- Comment / default documentation.

**L0056** ``

- Blank line.

**L0057** `# The full public facing url you use in browser, used for redirects and emails`

- Comment / default documentation.

**L0058** `# If you use reverse proxy and sub path specify full url (with sub path)`

- Comment / default documentation.

**L0059** `root_url = %(protocol)s://%(domain)s:%(http_port)s/`

- Full public URL Grafana uses in links.

**L0060** ``

- Blank line.

**L0061** `# Serve Grafana from subpath specified in \`root_url\` setting. By default it is set to \`false\` for compatibility reasons.`

- Comment / default documentation.

**L0062** `;serve_from_sub_path = false`

- Comment / default documentation.

**L0063** ``

- Blank line.

**L0064** `# Log web requests`

- Comment / default documentation.

**L0065** `;router_logging = false`

- Comment / default documentation.

**L0066** ``

- Blank line.

**L0067** `# the path relative working path`

- Comment / default documentation.

**L0068** `;static_root_path = public`

- Comment / default documentation.

**L0069** ``

- Blank line.

**L0070** `# enable gzip`

- Comment / default documentation.

**L0071** `enable_gzip = true`

- Enable gzip compression for HTTP responses.

**L0072** ``

- Blank line.

**L0073** `# https certs & key file`

- Comment / default documentation.

**L0074** `cert_file = /Users/anishskumar/Anish-DevOps-Lab/observability/grafana/certs/localhost.crt`

- TLS certificate path for HTTPS.

**L0075** `cert_key = /Users/anishskumar/Anish-DevOps-Lab/observability/grafana/certs/localhost.key`

- TLS private key path for HTTPS.

**L0076** ``

- Blank line.

**L0077** `# optional password to be used to decrypt key file`

- Comment / default documentation.

**L0078** `;cert_pass =`

- Comment / default documentation.

**L0079** ``

- Blank line.

**L0080** `# Certificates file watch interval`

- Comment / default documentation.

**L0081** `;certs_watch_interval =`

- Comment / default documentation.

**L0082** ``

- Blank line.

**L0083** `# Unix socket gid`

- Comment / default documentation.

**L0084** `# Changing the gid of a file without privileges requires that the target group is in the group of the process and that the process is the file owner`

- Comment / default documentation.

**L0085** `# It is recommended to set the gid as http server user gid`

- Comment / default documentation.

**L0086** `# Not set when the value is -1`

- Comment / default documentation.

**L0087** `;socket_gid =`

- Comment / default documentation.

**L0088** ``

- Blank line.

**L0089** `# Unix socket mode`

- Comment / default documentation.

**L0090** `;socket_mode =`

- Comment / default documentation.

**L0091** ``

- Blank line.

**L0092** `# Unix socket path`

- Comment / default documentation.

**L0093** `;socket =`

- Comment / default documentation.

**L0094** ``

- Blank line.

**L0095** `# CDN Url`

- Comment / default documentation.

**L0096** `;cdn_url =`

- Comment / default documentation.

**L0097** ``

- Blank line.

**L0098** `# Sets the maximum time using a duration format (5s/5m/5ms) before timing out read of an incoming request and closing idle connections.`

- Comment / default documentation.

**L0099** `# \`0\` means there is no timeout for reading the request.`

- Comment / default documentation.

**L0100** `read_timeout = 30s`

- Max time to read an incoming request.

**L0101** ``

- Blank line.

**L0102** `# This setting enables you to specify additional headers that the server adds to HTTP(S) responses.`

- Comment / default documentation.

**L0103** `[server.custom_response_headers]`

- Section header: server.custom_response_headers

**L0104** `#exampleHeader1 = exampleValue1`

- Comment / default documentation.

**L0105** `#exampleHeader2 = exampleValue2`

- Comment / default documentation.

**L0106** ``

- Blank line.

**L0107** `[environment]`

- Section header: environment

**L0108** `# Sets whether the local file system is available for Grafana to use. Default is true for backward compatibility.`

- Comment / default documentation.

**L0109** `;local_file_system_available = true`

- Comment / default documentation.

**L0110** ``

- Blank line.

**L0111** `#################################### GRPC Server #########################`

- Comment / default documentation.

**L0112** `;[grpc_server]`

- Comment / default documentation.

**L0113** `;network = "tcp"`

- Comment / default documentation.

**L0114** `;address = "127.0.0.1:10000"`

- Comment / default documentation.

**L0115** `;use_tls = false`

- Comment / default documentation.

**L0116** `;cert_file =`

- Comment / default documentation.

**L0117** `;key_file =`

- Comment / default documentation.

**L0118** `;max_recv_msg_size =`

- Comment / default documentation.

**L0119** `;max_send_msg_size =`

- Comment / default documentation.

**L0120** `# this will log the request and response for each unary gRPC call`

- Comment / default documentation.

**L0121** `;enable_logging = false`

- Comment / default documentation.

**L0122** `;max_connection_age =`

- Comment / default documentation.

**L0123** `;max_connection_age_grace =`

- Comment / default documentation.

**L0124** `;max_connection_idle =`

- Comment / default documentation.

**L0125** `;keepalive_time =`

- Comment / default documentation.

**L0126** `;keepalive_timeout =`

- Comment / default documentation.

**L0127** `;keepalive_min_time =`

- Comment / default documentation.

**L0128** ``

- Blank line.

**L0129** `#################################### Database ####################################`

- Comment / default documentation.

**L0130** `[database]`

- Section header: database

**L0131** `# You can configure the database connection by specifying type, host, name, user and password`

- Comment / default documentation.

**L0132** `# as separate properties or as on string using the url properties.`

- Comment / default documentation.

**L0133** ``

- Blank line.

**L0134** `# Either "mysql", "postgres" or "sqlite3", it's your choice`

- Comment / default documentation.

**L0135** `;type = sqlite3`

- Comment / default documentation.

**L0136** `;host = 127.0.0.1:3306`

- Comment / default documentation.

**L0137** `;name = grafana`

- Comment / default documentation.

**L0138** `;user = root`

- Comment / default documentation.

**L0139** `# If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""`

- Comment / default documentation.

**L0140** `;password =`

- Comment / default documentation.

**L0141** `# Use either URL or the previous fields to configure the database`

- Comment / default documentation.

**L0142** `# Example: mysql://user:secret@host:port/database`

- Comment / default documentation.

**L0143** `;url =`

- Comment / default documentation.

**L0144** ``

- Blank line.

**L0145** `# Set to true or false to enable or disable high availability mode.`

- Comment / default documentation.

**L0146** `# When it's set to false some functions will be simplified and only run in-process`

- Comment / default documentation.

**L0147** `# instead of relying on the database.`

- Comment / default documentation.

**L0148** `#`

- Comment / default documentation.

**L0149** `# Only set it to false if you run only a single instance of Grafana.`

- Comment / default documentation.

**L0150** `;high_availability = true`

- Comment / default documentation.

**L0151** ``

- Blank line.

**L0152** `# Max idle conn setting default is 2`

- Comment / default documentation.

**L0153** `;max_idle_conn = 2`

- Comment / default documentation.

**L0154** ``

- Blank line.

**L0155** `# Max conn setting default is 0 (mean not set)`

- Comment / default documentation.

**L0156** `;max_open_conn =`

- Comment / default documentation.

**L0157** ``

- Blank line.

**L0158** `# Connection Max Lifetime default is 14400 (means 14400 seconds or 4 hours)`

- Comment / default documentation.

**L0159** `;conn_max_lifetime = 14400`

- Comment / default documentation.

**L0160** ``

- Blank line.

**L0161** `# Set to true to log the sql calls and execution times.`

- Comment / default documentation.

**L0162** `;log_queries =`

- Comment / default documentation.

**L0163** ``

- Blank line.

**L0164** `# For "postgres", use either "disable", "require" or "verify-full"`

- Comment / default documentation.

**L0165** `# For "mysql", use either "true", "false", or "skip-verify".`

- Comment / default documentation.

**L0166** `;ssl_mode = disable`

- Comment / default documentation.

**L0167** ``

- Blank line.

**L0168** `# For "postgres", use either "1" to enable or "0" to disable SNI`

- Comment / default documentation.

**L0169** `;ssl_sni =`

- Comment / default documentation.

**L0170** ``

- Blank line.

**L0171** `# Database drivers may support different transaction isolation levels.`

- Comment / default documentation.

**L0172** `# Currently, only "mysql" driver supports isolation levels.`

- Comment / default documentation.

**L0173** `# If the value is empty - driver's default isolation level is applied.`

- Comment / default documentation.

**L0174** `# For "mysql" use "READ-UNCOMMITTED", "READ-COMMITTED", "REPEATABLE-READ" or "SERIALIZABLE".`

- Comment / default documentation.

**L0175** `;isolation_level =`

- Comment / default documentation.

**L0176** ``

- Blank line.

**L0177** `;ca_cert_path =`

- Comment / default documentation.

**L0178** `;client_key_path =`

- Comment / default documentation.

**L0179** `;client_cert_path =`

- Comment / default documentation.

**L0180** `;server_cert_name =`

- Comment / default documentation.

**L0181** ``

- Blank line.

**L0182** `# For "sqlite3" only, path relative to data_path setting`

- Comment / default documentation.

**L0183** `;path = grafana.db`

- Comment / default documentation.

**L0184** ``

- Blank line.

**L0185** `# For "sqlite3" only. cache mode setting used for connecting to the database. (private, shared)`

- Comment / default documentation.

**L0186** `;cache_mode = private`

- Comment / default documentation.

**L0187** ``

- Blank line.

**L0188** `# For "sqlite3" only. Enable/disable Write-Ahead Logging, https://sqlite.org/wal.html. Default is false.`

- Comment / default documentation.

**L0189** `;wal = false`

- Comment / default documentation.

**L0190** ``

- Blank line.

**L0191** `# For "mysql" and "postgres" only. Lock the database for the migrations, default is true.`

- Comment / default documentation.

**L0192** `;migration_locking = true`

- Comment / default documentation.

**L0193** ``

- Blank line.

**L0194** `# For "mysql" and "postgres" only. How many seconds to wait before failing to lock the database for the migrations, default is 0.`

- Comment / default documentation.

**L0195** `;locking_attempt_timeout_sec = 0`

- Comment / default documentation.

**L0196** ``

- Blank line.

**L0197** `# For "sqlite" only. How many times to retry query in case of database is locked failures. Default is 0 (disabled).`

- Comment / default documentation.

**L0198** `;query_retries = 0`

- Comment / default documentation.

**L0199** ``

- Blank line.

**L0200** `# For "sqlite" only. How many times to retry transaction in case of database is locked failures. Default is 5.`

- Comment / default documentation.

**L0201** `;transaction_retries = 5`

- Comment / default documentation.

**L0202** ``

- Blank line.

**L0203** `# Set to true to add metrics and tracing for database queries.`

- Comment / default documentation.

**L0204** `;instrument_queries = false`

- Comment / default documentation.

**L0205** ``

- Blank line.

**L0206** `# Set to true to delete auto-generated primary keys during migrations.`

- Comment / default documentation.

**L0207** `# This is useful when databases have auto-generated primary keys enabled.`

- Comment / default documentation.

**L0208** `;delete_auto_gen_ids = false`

- Comment / default documentation.

**L0209** ``

- Blank line.

**L0210** `# Set to true to skip dashboard UID migrations on startup.`

- Comment / default documentation.

**L0211** `# Improves startup performance for instances with large numbers of annotations who do not plan to downgrade Grafana.`

- Comment / default documentation.

**L0212** `;skip_dashboard_uid_migration_on_startup = false`

- Comment / default documentation.

**L0213** ``

- Blank line.

**L0214** `#################################### Cache server #############################`

- Comment / default documentation.

**L0215** `[remote_cache]`

- Section header: remote_cache

**L0216** `# Either "redis", "memcached" or "database" default is "database"`

- Comment / default documentation.

**L0217** `type = database`

- Remote cache backend type.

**L0218** ``

- Blank line.

**L0219** `# cache connectionstring options`

- Comment / default documentation.

**L0220** `# database: will use Grafana primary database.`

- Comment / default documentation.

**L0221** `# redis: config like redis server e.g. \`addr=127.0.0.1:6379,pool_size=100,db=0,username=grafana,password=grafanaRocks,ssl=false\`. Only addr is required. ssl may be 'true', 'false', or 'insecure'.`

- Comment / default documentation.

**L0222** `# memcache: 127.0.0.1:11211`

- Comment / default documentation.

**L0223** `;connstr =`

- Comment / default documentation.

**L0224** ``

- Blank line.

**L0225** `# prefix prepended to all the keys in the remote cache`

- Comment / default documentation.

**L0226** `; prefix =`

- Comment / default documentation.

**L0227** ``

- Blank line.

**L0228** `# This enables encryption of values stored in the remote cache`

- Comment / default documentation.

**L0229** `;encryption =`

- Comment / default documentation.

**L0230** ``

- Blank line.

**L0231** `#################################### Data proxy ###########################`

- Comment / default documentation.

**L0232** `[dataproxy]`

- Section header: dataproxy

**L0233** ``

- Blank line.

**L0234** `# This enables data proxy logging, default is false`

- Comment / default documentation.

**L0235** `;logging = false`

- Comment / default documentation.

**L0236** ``

- Blank line.

**L0237** `# How long the data proxy waits to read the headers of the response before timing out, default is 30 seconds.`

- Comment / default documentation.

**L0238** `# This setting also applies to core backend HTTP data sources where query requests use an HTTP client with timeout set.`

- Comment / default documentation.

**L0239** `timeout = 30`

- Data proxy request timeout (seconds).

**L0240** ``

- Blank line.

**L0241** `# How long the data proxy waits to establish a TCP connection before timing out, default is 10 seconds.`

- Comment / default documentation.

**L0242** `;dialTimeout = 10`

- Comment / default documentation.

**L0243** ``

- Blank line.

**L0244** `# How many seconds the data proxy waits before sending a keepalive probe request.`

- Comment / default documentation.

**L0245** `;keep_alive_seconds = 30`

- Comment / default documentation.

**L0246** ``

- Blank line.

**L0247** `# How many seconds the data proxy waits for a successful TLS Handshake before timing out.`

- Comment / default documentation.

**L0248** `;tls_handshake_timeout_seconds = 10`

- Comment / default documentation.

**L0249** ``

- Blank line.

**L0250** `# How many seconds the data proxy will wait for a server's first response headers after`

- Comment / default documentation.

**L0251** `# fully writing the request headers if the request has an "Expect: 100-continue"`

- Comment / default documentation.

**L0252** `# header. A value of 0 will result in the body being sent immediately, without`

- Comment / default documentation.

**L0253** `# waiting for the server to approve.`

- Comment / default documentation.

**L0254** `;expect_continue_timeout_seconds = 1`

- Comment / default documentation.

**L0255** ``

- Blank line.

**L0256** `# Optionally limits the total number of connections per host, including connections in the dialing,`

- Comment / default documentation.

**L0257** `# active, and idle states. On limit violation, dials will block.`

- Comment / default documentation.

**L0258** `# A value of zero (0) means no limit.`

- Comment / default documentation.

**L0259** `;max_conns_per_host = 0`

- Comment / default documentation.

**L0260** ``

- Blank line.

**L0261** `# The maximum number of idle connections that Grafana will keep alive.`

- Comment / default documentation.

**L0262** `;max_idle_connections = 100`

- Comment / default documentation.

**L0263** ``

- Blank line.

**L0264** `# How many seconds the data proxy keeps an idle connection open before timing out.`

- Comment / default documentation.

**L0265** `;idle_conn_timeout_seconds = 90`

- Comment / default documentation.

**L0266** ``

- Blank line.

**L0267** `# If enabled and user is not anonymous, data proxy will add X-Grafana-User header with username into the request, default is false.`

- Comment / default documentation.

**L0268** `;send_user_header = false`

- Comment / default documentation.

**L0269** ``

- Blank line.

**L0270** `# Limit the amount of bytes that will be read/accepted from responses of outgoing HTTP requests.`

- Comment / default documentation.

**L0271** `;response_limit = 0`

- Comment / default documentation.

**L0272** ``

- Blank line.

**L0273** `# Limits the number of rows that Grafana will process from SQL data sources.`

- Comment / default documentation.

**L0274** `;row_limit = 1000000`

- Comment / default documentation.

**L0275** ``

- Blank line.

**L0276** `# Sets a custom value for the \`User-Agent\` header for outgoing data proxy requests. If empty, the default value is \`Grafana/<BuildVersion>\` (for example \`Grafana/9.0.0\`).`

- Comment / default documentation.

**L0277** `;user_agent =`

- Comment / default documentation.

**L0278** ``

- Blank line.

**L0279** `#################################### Analytics ####################################`

- Comment / default documentation.

**L0280** `[analytics]`

- Section header: analytics

**L0281** `# Server reporting, sends usage counters to stats.grafana.org every 24 hours.`

- Comment / default documentation.

**L0282** `# No ip addresses are being tracked, only simple counters to track`

- Comment / default documentation.

**L0283** `# running instances, dashboard and error counts. It is very helpful to us.`

- Comment / default documentation.

**L0284** `# Change this option to false to disable reporting.`

- Comment / default documentation.

**L0285** `;reporting_enabled = true`

- Comment / default documentation.

**L0286** ``

- Blank line.

**L0287** `# The name of the distributor of the Grafana instance. Ex hosted-grafana, grafana-labs`

- Comment / default documentation.

**L0288** `;reporting_distributor = grafana-labs`

- Comment / default documentation.

**L0289** ``

- Blank line.

**L0290** `# Set to false to disable all checks to https://grafana.com`

- Comment / default documentation.

**L0291** `# for new versions of grafana. The check is used`

- Comment / default documentation.

**L0292** `# in some UI views to notify that a grafana update exists.`

- Comment / default documentation.

**L0293** `# This option does not cause any auto updates, nor send any information`

- Comment / default documentation.

**L0294** `# only a GET request to https://grafana.com/api/grafana/versions/stable to get the latest version.`

- Comment / default documentation.

**L0295** `;check_for_updates = true`

- Comment / default documentation.

**L0296** ``

- Blank line.

**L0297** `# Set to false to disable all checks to https://grafana.com`

- Comment / default documentation.

**L0298** `# for new versions of plugins. The check is used`

- Comment / default documentation.

**L0299** `# in some UI views to notify that a plugin update exists.`

- Comment / default documentation.

**L0300** `# This option does not cause any auto updates, nor send any information`

- Comment / default documentation.

**L0301** `# only a GET request to https://grafana.com to get the latest versions.`

- Comment / default documentation.

**L0302** `;check_for_plugin_updates = true`

- Comment / default documentation.

**L0303** ``

- Blank line.

**L0304** `# Google Analytics universal tracking code, only enabled if you specify an id here`

- Comment / default documentation.

**L0305** `;google_analytics_ua_id =`

- Comment / default documentation.

**L0306** ``

- Blank line.

**L0307** `# Google Analytics 4 tracking code, only enabled if you specify an id here`

- Comment / default documentation.

**L0308** `;google_analytics_4_id =`

- Comment / default documentation.

**L0309** ``

- Blank line.

**L0310** `# When Google Analytics 4 Enhanced event measurement is enabled, we will try to avoid sending duplicate events and let Google Analytics 4 detect navigation changes, etc.`

- Comment / default documentation.

**L0311** `;google_analytics_4_send_manual_page_views = false`

- Comment / default documentation.

**L0312** ``

- Blank line.

**L0313** `# Google Tag Manager ID, only enabled if you specify an id here`

- Comment / default documentation.

**L0314** `;google_tag_manager_id =`

- Comment / default documentation.

**L0315** ``

- Blank line.

**L0316** `# Rudderstack write key, enabled only if rudderstack_data_plane_url is also set`

- Comment / default documentation.

**L0317** `;rudderstack_write_key =`

- Comment / default documentation.

**L0318** ``

- Blank line.

**L0319** `# Rudderstack data plane url, enabled only if rudderstack_write_key is also set`

- Comment / default documentation.

**L0320** `;rudderstack_data_plane_url =`

- Comment / default documentation.

**L0321** ``

- Blank line.

**L0322** `# Rudderstack SDK url, optional, only valid if rudderstack_write_key and rudderstack_data_plane_url is also set`

- Comment / default documentation.

**L0323** `;rudderstack_sdk_url =`

- Comment / default documentation.

**L0324** ``

- Blank line.

**L0325** `# Rudderstack Config url, optional, used by Rudderstack SDK to fetch source config`

- Comment / default documentation.

**L0326** `;rudderstack_config_url =`

- Comment / default documentation.

**L0327** ``

- Blank line.

**L0328** `# Rudderstack Integrations URL, optional. Only valid if you pass the SDK version 1.1 or higher`

- Comment / default documentation.

**L0329** `;rudderstack_integrations_url =`

- Comment / default documentation.

**L0330** ``

- Blank line.

**L0331** `# Intercom secret, optional, used to hash user_id before passing to Intercom via Rudderstack`

- Comment / default documentation.

**L0332** `;intercom_secret =`

- Comment / default documentation.

**L0333** ``

- Blank line.

**L0334** `# Application Insights connection string. Specify an URL string to enable this feature.`

- Comment / default documentation.

**L0335** `;application_insights_connection_string =`

- Comment / default documentation.

**L0336** ``

- Blank line.

**L0337** `# Optional. Specifies an Application Insights endpoint URL where the endpoint string is wrapped in backticks \`\`.`

- Comment / default documentation.

**L0338** `;application_insights_endpoint_url =`

- Comment / default documentation.

**L0339** ``

- Blank line.

**L0340** `# Controls if the UI contains any links to user feedback forms`

- Comment / default documentation.

**L0341** `;feedback_links_enabled = true`

- Comment / default documentation.

**L0342** ``

- Blank line.

**L0343** `# Static context that is being added to analytics events`

- Comment / default documentation.

**L0344** `;reporting_static_context = grafanaInstance=12, os=linux`

- Comment / default documentation.

**L0345** ``

- Blank line.

**L0346** `# Logs interaction events to the browser javascript console, intended for development only`

- Comment / default documentation.

**L0347** `;browser_console_reporter = false`

- Comment / default documentation.

**L0348** ``

- Blank line.

**L0349** `#################################### Security ####################################`

- Comment / default documentation.

**L0350** `[security]`

- Section header: security

**L0351** `# disable creation of admin user on first start of grafana`

- Comment / default documentation.

**L0352** `;disable_initial_admin_creation = false`

- Comment / default documentation.

**L0353** ``

- Blank line.

**L0354** `# default admin user, created on startup`

- Comment / default documentation.

**L0355** `;admin_user = admin`

- Comment / default documentation.

**L0356** ``

- Blank line.

**L0357** `# default admin password, can be changed before first start of grafana,  or in profile settings`

- Comment / default documentation.

**L0358** `;admin_password = admin`

- Comment / default documentation.

**L0359** ``

- Blank line.

**L0360** `# default admin email, created on startup`

- Comment / default documentation.

**L0361** `;admin_email = admin@localhost`

- Comment / default documentation.

**L0362** ``

- Blank line.

**L0363** `# used for signing`

- Comment / default documentation.

**L0364** `;secret_key = SW2YcwTIb9zpOOhoPsMm`

- Comment / default documentation.

**L0365** ``

- Blank line.

**L0366** `# current key provider used for envelope encryption, default to static value specified by secret_key`

- Comment / default documentation.

**L0367** `;encryption_provider = secretKey.v1`

- Comment / default documentation.

**L0368** ``

- Blank line.

**L0369** `# list of configured key providers, space separated (Enterprise only): e.g., awskms.v1 azurekv.v1`

- Comment / default documentation.

**L0370** `;available_encryption_providers =`

- Comment / default documentation.

**L0371** ``

- Blank line.

**L0372** `# disable gravatar profile images`

- Comment / default documentation.

**L0373** `;disable_gravatar = false`

- Comment / default documentation.

**L0374** ``

- Blank line.

**L0375** `# data source proxy whitelist (ip_or_domain:port separated by spaces)`

- Comment / default documentation.

**L0376** `;data_source_proxy_whitelist =`

- Comment / default documentation.

**L0377** ``

- Blank line.

**L0378** `# disable protection against brute force login attempts`

- Comment / default documentation.

**L0379** `;disable_brute_force_login_protection = false`

- Comment / default documentation.

**L0380** ``

- Blank line.

**L0381** `# max number of failed login attempts before user gets locked`

- Comment / default documentation.

**L0382** `;brute_force_login_protection_max_attempts = 5`

- Comment / default documentation.

**L0383** ``

- Blank line.

**L0384** `# disable protection against brute force login attempts by username`

- Comment / default documentation.

**L0385** `;disable_username_login_protection = false`

- Comment / default documentation.

**L0386** ``

- Blank line.

**L0387** `# disable protection against brute force login attempts by IP address`

- Comment / default documentation.

**L0388** `; disable_ip_address_login_protection = true`

- Comment / default documentation.

**L0389** ``

- Blank line.

**L0390** `# set to true if you host Grafana behind HTTPS. default is false.`

- Comment / default documentation.

**L0391** `;cookie_secure = false`

- Comment / default documentation.

**L0392** ``

- Blank line.

**L0393** `# set cookie SameSite attribute. defaults to \`lax\`. can be set to "lax", "strict", "none" and "disabled"`

- Comment / default documentation.

**L0394** `;cookie_samesite = lax`

- Comment / default documentation.

**L0395** ``

- Blank line.

**L0396** `# set to true if you want to allow browsers to render Grafana in a <frame>, <iframe>, <embed> or <object>. default is false.`

- Comment / default documentation.

**L0397** `;allow_embedding = false`

- Comment / default documentation.

**L0398** ``

- Blank line.

**L0399** `# Set to true if you want to enable http strict transport security (HSTS) response header.`

- Comment / default documentation.

**L0400** `# HSTS tells browsers that the site should only be accessed using HTTPS.`

- Comment / default documentation.

**L0401** `;strict_transport_security = false`

- Comment / default documentation.

**L0402** ``

- Blank line.

**L0403** `# Sets how long a browser should cache HSTS. Only applied if strict_transport_security is enabled.`

- Comment / default documentation.

**L0404** `;strict_transport_security_max_age_seconds = 86400`

- Comment / default documentation.

**L0405** ``

- Blank line.

**L0406** `# Set to true if to enable HSTS preloading option. Only applied if strict_transport_security is enabled.`

- Comment / default documentation.

**L0407** `;strict_transport_security_preload = false`

- Comment / default documentation.

**L0408** ``

- Blank line.

**L0409** `# Set to true if to enable the HSTS includeSubDomains option. Only applied if strict_transport_security is enabled.`

- Comment / default documentation.

**L0410** `;strict_transport_security_subdomains = false`

- Comment / default documentation.

**L0411** ``

- Blank line.

**L0412** `# Set to true to enable the X-Content-Type-Options response header.`

- Comment / default documentation.

**L0413** `# The X-Content-Type-Options response HTTP header is a marker used by the server to indicate that the MIME types advertised`

- Comment / default documentation.

**L0414** `# in the Content-Type headers should not be changed and be followed.`

- Comment / default documentation.

**L0415** `;x_content_type_options = true`

- Comment / default documentation.

**L0416** ``

- Blank line.

**L0417** `# Set to true to enable the X-XSS-Protection header, which tells browsers to stop pages from loading`

- Comment / default documentation.

**L0418** `# when they detect reflected cross-site scripting (XSS) attacks.`

- Comment / default documentation.

**L0419** `;x_xss_protection = true`

- Comment / default documentation.

**L0420** ``

- Blank line.

**L0421** `# Enable adding the Content-Security-Policy header to your requests.`

- Comment / default documentation.

**L0422** `# CSP allows to control resources the user agent is allowed to load and helps prevent XSS attacks.`

- Comment / default documentation.

**L0423** `;content_security_policy = false`

- Comment / default documentation.

**L0424** ``

- Blank line.

**L0425** `# Set Content Security Policy template used when adding the Content-Security-Policy header to your requests.`

- Comment / default documentation.

**L0426** `# $NONCE in the template includes a random nonce.`

- Comment / default documentation.

**L0427** `# $ROOT_PATH is server.root_url without the protocol.`

- Comment / default documentation.

**L0428** `;content_security_policy_template = """script-src 'self' 'unsafe-eval' 'unsafe-inline' 'strict-dynamic' $NONCE;object-src 'none';font-src 'self';style-src 'self' 'unsafe-inline' blob:;img-src * data:;base-uri 'self';connect-src 'self' grafana.com ws://$ROOT_PATH wss://$ROOT_PATH;manifest-src 'self';media-src 'none';form-action 'self';"""`

- Comment / default documentation.

**L0429** ``

- Blank line.

**L0430** `# Enable adding the Content-Security-Policy-Report-Only header to your requests.`

- Comment / default documentation.

**L0431** `# Allows you to monitor the effects of a policy without enforcing it.`

- Comment / default documentation.

**L0432** `;content_security_policy_report_only = false`

- Comment / default documentation.

**L0433** ``

- Blank line.

**L0434** `# Set Content Security Policy Report Only template used when adding the Content-Security-Policy-Report-Only header to your requests.`

- Comment / default documentation.

**L0435** `# $NONCE in the template includes a random nonce.`

- Comment / default documentation.

**L0436** `# $ROOT_PATH is server.root_url without the protocol.`

- Comment / default documentation.

**L0437** `;content_security_policy_report_only_template = """script-src 'self' 'unsafe-eval' 'unsafe-inline' 'strict-dynamic' $NONCE;object-src 'none';font-src 'self';style-src 'self' 'unsafe-inline' blob:;img-src * data:;base-uri 'self';connect-src 'self' grafana.com ws://$ROOT_PATH wss://$ROOT_PATH;manifest-src 'self';media-src 'none';form-action 'self';"""`

- Comment / default documentation.

**L0438** ``

- Blank line.

**L0439** `# List of additional allowed URLs to pass by the CSRF check, separated by spaces. Suggested when authentication comes from an IdP.`

- Comment / default documentation.

**L0440** `;csrf_trusted_origins = example.com`

- Comment / default documentation.

**L0441** ``

- Blank line.

**L0442** `# List of allowed headers to be set by the user, separated by spaces. Suggested to use for if authentication lives behind reverse proxies.`

- Comment / default documentation.

**L0443** `;csrf_additional_headers =`

- Comment / default documentation.

**L0444** ``

- Blank line.

**L0445** `# The CSRF check will be executed even if the request has no login cookie.`

- Comment / default documentation.

**L0446** `;csrf_always_check = false`

- Comment / default documentation.

**L0447** ``

- Blank line.

**L0448** `# Comma-separated list of plugins ids that will be loaded inside the frontend sandbox`

- Comment / default documentation.

**L0449** `# Currently behind the feature flag pluginsFrontendSandbox`

- Comment / default documentation.

**L0450** `;enable_frontend_sandbox_for_plugins =`

- Comment / default documentation.

**L0451** ``

- Blank line.

**L0452** `# Comma-separated list of paths for POST/PUT URL in actions. Empty will allow anything that is not on the same origin`

- Comment / default documentation.

**L0453** `;actions_allow_post_url =`

- Comment / default documentation.

**L0454** ``

- Blank line.

**L0455** `[security.encryption]`

- Section header: security.encryption

**L0456** `# Defines the time-to-live (TTL) for decrypted data encryption keys stored in memory (cache).`

- Comment / default documentation.

**L0457** `# Please note that small values may cause performance issues due to a high frequency decryption operations.`

- Comment / default documentation.

**L0458** `;data_keys_cache_ttl = 15m`

- Comment / default documentation.

**L0459** ``

- Blank line.

**L0460** `# Defines the frequency of data encryption keys cache cleanup interval.`

- Comment / default documentation.

**L0461** `# On every interval, decrypted data encryption keys that reached the TTL are removed from the cache.`

- Comment / default documentation.

**L0462** `;data_keys_cache_cleanup_interval = 1m`

- Comment / default documentation.

**L0463** ``

- Blank line.

**L0464** `#################################### Snapshots ###########################`

- Comment / default documentation.

**L0465** `[snapshots]`

- Section header: snapshots

**L0466** `# set to false to remove snapshot functionality`

- Comment / default documentation.

**L0467** `;enabled = true`

- Comment / default documentation.

**L0468** ``

- Blank line.

**L0469** `# snapshot sharing options`

- Comment / default documentation.

**L0470** `;external_enabled = true`

- Comment / default documentation.

**L0471** `;external_snapshot_url = https://snapshots.raintank.io`

- Comment / default documentation.

**L0472** `;external_snapshot_name = Publish to snapshots.raintank.io`

- Comment / default documentation.

**L0473** ``

- Blank line.

**L0474** `# Set to true to enable this Grafana instance act as an external snapshot server and allow unauthenticated requests for`

- Comment / default documentation.

**L0475** `# creating and deleting snapshots.`

- Comment / default documentation.

**L0476** `;public_mode = false`

- Comment / default documentation.

**L0477** ``

- Blank line.

**L0478** `#################################### Dashboards ##################`

- Comment / default documentation.

**L0479** `[dashboards]`

- Section header: dashboards

**L0480** `# Number dashboard versions to keep (per dashboard). Default: 20, Minimum: 1`

- Comment / default documentation.

**L0481** `;versions_to_keep = 20`

- Comment / default documentation.

**L0482** ``

- Blank line.

**L0483** `# Minimum dashboard refresh interval. When set, this will restrict users to set the refresh interval of a dashboard lower than given interval. Per default this is 5 seconds.`

- Comment / default documentation.

**L0484** `# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L0485** `min_refresh_interval = 10s`

- Minimum allowed dashboard refresh interval.

**L0486** ``

- Blank line.

**L0487** `# Path to the default home dashboard. If this value is empty, then Grafana uses StaticRootPath + "dashboards/home.json"`

- Comment / default documentation.

**L0488** `;default_home_dashboard_path =`

- Comment / default documentation.

**L0489** ``

- Blank line.

**L0490** `################################### Data sources #########################`

- Comment / default documentation.

**L0491** `[datasources]`

- Section header: datasources

**L0492** `# Upper limit of data sources that Grafana will return. This limit is a temporary configuration and it will be deprecated when pagination will be introduced on the list data sources API.`

- Comment / default documentation.

**L0493** `;datasource_limit = 5000`

- Comment / default documentation.

**L0494** ``

- Blank line.

**L0495** `# Number of queries to be executed concurrently. Only for the datasource supports concurrency.`

- Comment / default documentation.

**L0496** `# For now only Loki and InfluxDB (with influxql) are supporting concurrency behind the feature flags.`

- Comment / default documentation.

**L0497** `# Check datasource documentations for enabling concurrency.`

- Comment / default documentation.

**L0498** `concurrent_query_count = 5`

- Limit concurrent datasource queries.

**L0499** ``

- Blank line.

**L0500** `# Default behavior for the "Manage alerts via Alerting UI" toggle when configuring a data source.`

- Comment / default documentation.

**L0501** `# It only works if the data source's \`jsonData.manageAlerts\` prop does not contain a previously configured value.`

- Comment / default documentation.

**L0502** `;default_manage_alerts_ui_toggle = true`

- Comment / default documentation.

**L0503** ``

- Blank line.

**L0504** `# Default behavior for the "Allow as recording rules target" toggle when configuring a data source.`

- Comment / default documentation.

**L0505** `# It only works if the data source's \`jsonData.allowAsRecordingRulesTarget\` prop does not contain a previously configured value.`

- Comment / default documentation.

**L0506** `;default_allow_recording_rules_target_alerts_ui_toggle = true`

- Comment / default documentation.

**L0507** ``

- Blank line.

**L0508** `################################### SQL Data Sources #####################`

- Comment / default documentation.

**L0509** `[sql_datasources]`

- Section header: sql_datasources

**L0510** `# Default maximum number of open connections maintained in the connection pool`

- Comment / default documentation.

**L0511** `# when connecting to SQL based data sources`

- Comment / default documentation.

**L0512** `;max_open_conns_default = 100`

- Comment / default documentation.

**L0513** ``

- Blank line.

**L0514** `# Default maximum number of idle connections maintained in the connection pool`

- Comment / default documentation.

**L0515** `# when connecting to SQL based data sources`

- Comment / default documentation.

**L0516** `;max_idle_conns_default = 100`

- Comment / default documentation.

**L0517** ``

- Blank line.

**L0518** `# Default maximum connection lifetime used when connecting`

- Comment / default documentation.

**L0519** `# to SQL based data sources.`

- Comment / default documentation.

**L0520** `;max_conn_lifetime_default = 14400`

- Comment / default documentation.

**L0521** ``

- Blank line.

**L0522** `#################################### Users ###############################`

- Comment / default documentation.

**L0523** `[users]`

- Section header: users

**L0524** `# disable user signup / registration`

- Comment / default documentation.

**L0525** `;allow_sign_up = true`

- Comment / default documentation.

**L0526** ``

- Blank line.

**L0527** `# Allow non admin users to create organizations`

- Comment / default documentation.

**L0528** `;allow_org_create = true`

- Comment / default documentation.

**L0529** ``

- Blank line.

**L0530** `# Set to true to automatically assign new users to the default organization (id 1)`

- Comment / default documentation.

**L0531** `;auto_assign_org = true`

- Comment / default documentation.

**L0532** ``

- Blank line.

**L0533** `# Set this value to automatically add new users to the provided organization (if auto_assign_org above is set to true)`

- Comment / default documentation.

**L0534** `;auto_assign_org_id = 1`

- Comment / default documentation.

**L0535** ``

- Blank line.

**L0536** `# Default role new users will be automatically assigned`

- Comment / default documentation.

**L0537** `;auto_assign_org_role = Viewer`

- Comment / default documentation.

**L0538** ``

- Blank line.

**L0539** `# Require email validation before sign up completes`

- Comment / default documentation.

**L0540** `;verify_email_enabled = false`

- Comment / default documentation.

**L0541** ``

- Blank line.

**L0542** `# Redirect to default OrgId after login`

- Comment / default documentation.

**L0543** `;login_default_org_id =`

- Comment / default documentation.

**L0544** ``

- Blank line.

**L0545** `# Background text for the user field on the login page`

- Comment / default documentation.

**L0546** `;login_hint = email or username`

- Comment / default documentation.

**L0547** `;password_hint = password`

- Comment / default documentation.

**L0548** ``

- Blank line.

**L0549** `# Default UI theme ("dark", "light" or "system")`

- Comment / default documentation.

**L0550** `;default_theme = dark`

- Comment / default documentation.

**L0551** ``

- Blank line.

**L0552** `# Default UI language (supported IETF language tag, such as en-US)`

- Comment / default documentation.

**L0553** `;default_language = en-US`

- Comment / default documentation.

**L0554** ``

- Blank line.

**L0555** `# Path to a custom home page. Users are only redirected to this if the default home dashboard is used. It should match a frontend route and contain a leading slash.`

- Comment / default documentation.

**L0556** `;home_page =`

- Comment / default documentation.

**L0557** ``

- Blank line.

**L0558** `# External user management, these options affect the organization users view`

- Comment / default documentation.

**L0559** `;external_manage_link_url =`

- Comment / default documentation.

**L0560** `;external_manage_link_name =`

- Comment / default documentation.

**L0561** `;external_manage_info =`

- Comment / default documentation.

**L0562** ``

- Blank line.

**L0563** ``

- Blank line.

**L0564** `# Deprecated: Assign your viewers to editors.`

- Comment / default documentation.

**L0565** `# Viewers can edit/inspect dashboard settings in the browser. But not save the dashboard.`

- Comment / default documentation.

**L0566** `;viewers_can_edit = false`

- Comment / default documentation.

**L0567** ``

- Blank line.

**L0568** `# Deprecated: Assign your editors to admins.`

- Comment / default documentation.

**L0569** `# Editors can administrate dashboard, folders and teams they create`

- Comment / default documentation.

**L0570** `;editors_can_admin = false`

- Comment / default documentation.

**L0571** ``

- Blank line.

**L0572** `# The duration in time a user invitation remains valid before expiring. This setting should be expressed as a duration. Examples: 6h (hours), 2d (days), 1w (week). Default is 24h (24 hours). The minimum supported duration is 15m (15 minutes).`

- Comment / default documentation.

**L0573** `;user_invite_max_lifetime_duration = 24h`

- Comment / default documentation.

**L0574** ``

- Blank line.

**L0575** `# The duration in time a verification email, used to update the email address of a user, remains valid before expiring. This setting should be expressed as a duration. Examples: 6h (hours), 2d (days), 1w (week). Default is 1h (1 hour).`

- Comment / default documentation.

**L0576** `;verification_email_max_lifetime_duration = 1h`

- Comment / default documentation.

**L0577** ``

- Blank line.

**L0578** `# Frequency of updating a user's last seen time. The minimum supported duration is 5m (5 minutes). The maximum supported duration is 1h (1 hour).`

- Comment / default documentation.

**L0579** `;last_seen_update_interval = 15m`

- Comment / default documentation.

**L0580** ``

- Blank line.

**L0581** `# Enter a comma-separated list of users login to hide them in the Grafana UI. These users are shown to Grafana admins and themselves.`

- Comment / default documentation.

**L0582** `; hidden_users =`

- Comment / default documentation.

**L0583** ``

- Blank line.

**L0584** `[secretscan]`

- Section header: secretscan

**L0585** `# Enable secretscan feature`

- Comment / default documentation.

**L0586** `;enabled = false`

- Comment / default documentation.

**L0587** ``

- Blank line.

**L0588** `# Interval to check for token leaks`

- Comment / default documentation.

**L0589** `;interval = 5m`

- Comment / default documentation.

**L0590** ``

- Blank line.

**L0591** `# base URL of the grafana token leak check service`

- Comment / default documentation.

**L0592** `;base_url = https://secret-scanning.grafana.net`

- Comment / default documentation.

**L0593** ``

- Blank line.

**L0594** `# URL to send outgoing webhooks to in case of detection`

- Comment / default documentation.

**L0595** `;oncall_url =`

- Comment / default documentation.

**L0596** ``

- Blank line.

**L0597** `# Whether to revoke the token if a leak is detected or just send a notification`

- Comment / default documentation.

**L0598** `;revoke = true`

- Comment / default documentation.

**L0599** ``

- Blank line.

**L0600** `[service_accounts]`

- Section header: service_accounts

**L0601** `# Service account maximum expiration date in days.`

- Comment / default documentation.

**L0602** `# When set, Grafana will not allow the creation of tokens with expiry greater than this setting.`

- Comment / default documentation.

**L0603** `; token_expiration_day_limit =`

- Comment / default documentation.

**L0604** ``

- Blank line.

**L0605** `[auth]`

- Section header: auth

**L0606** `# Login cookie name`

- Comment / default documentation.

**L0607** `;login_cookie_name = grafana_session`

- Comment / default documentation.

**L0608** ``

- Blank line.

**L0609** `# Disable usage of Grafana build-in login solution.`

- Comment / default documentation.

**L0610** `;disable_login = false`

- Comment / default documentation.

**L0611** ``

- Blank line.

**L0612** `# The maximum lifetime (duration) an authenticated user can be inactive before being required to login at next visit. Default is 7 days (7d). This setting should be expressed as a duration, e.g. 5m (minutes), 6h (hours), 10d (days), 2w (weeks), 1M (month). The lifetime resets at each successful token rotation.`

- Comment / default documentation.

**L0613** `;login_maximum_inactive_lifetime_duration =`

- Comment / default documentation.

**L0614** ``

- Blank line.

**L0615** `# The maximum lifetime (duration) an authenticated user can be logged in since login time before being required to login. Default is 30 days (30d). This setting should be expressed as a duration, e.g. 5m (minutes), 6h (hours), 10d (days), 2w (weeks), 1M (month).`

- Comment / default documentation.

**L0616** `;login_maximum_lifetime_duration =`

- Comment / default documentation.

**L0617** ``

- Blank line.

**L0618** `# How often should auth tokens be rotated for authenticated users when being active. The default is each 10 minutes.`

- Comment / default documentation.

**L0619** `;token_rotation_interval_minutes = 10`

- Comment / default documentation.

**L0620** ``

- Blank line.

**L0621** `# Set to true to disable (hide) the login form, useful if you use OAuth, defaults to false`

- Comment / default documentation.

**L0622** `;disable_login_form = false`

- Comment / default documentation.

**L0623** ``

- Blank line.

**L0624** `# Set to true to disable the sign out link in the side menu. Useful if you use auth.proxy or auth.jwt, defaults to false`

- Comment / default documentation.

**L0625** `;disable_signout_menu = false`

- Comment / default documentation.

**L0626** ``

- Blank line.

**L0627** `# URL to redirect the user to after sign out`

- Comment / default documentation.

**L0628** `;signout_redirect_url =`

- Comment / default documentation.

**L0629** ``

- Blank line.

**L0630** `# Set to true to attempt login with OAuth automatically, skipping the login screen.`

- Comment / default documentation.

**L0631** `# This setting is ignored if multiple OAuth providers are configured.`

- Comment / default documentation.

**L0632** `# Deprecated, use auto_login option for specific provider instead.`

- Comment / default documentation.

**L0633** `;oauth_auto_login = false`

- Comment / default documentation.

**L0634** ``

- Blank line.

**L0635** `# Sets a custom oAuth error message. This is useful if you need to point the users to a specific location for support.`

- Comment / default documentation.

**L0636** `;oauth_login_error_message = oauth.login.error`

- Comment / default documentation.

**L0637** ``

- Blank line.

**L0638** `# OAuth state max age cookie duration in seconds. Defaults to 600 seconds.`

- Comment / default documentation.

**L0639** `;oauth_state_cookie_max_age = 600`

- Comment / default documentation.

**L0640** ``

- Blank line.

**L0641** `# Minimum wait time in milliseconds for the server lock retry mechanism.`

- Comment / default documentation.

**L0642** `# The server lock retry mechanism is used to prevent multiple Grafana instances from`

- Comment / default documentation.

**L0643** `# simultaneously refreshing OAuth tokens. This mechanism waits at least this amount`

- Comment / default documentation.

**L0644** `# of time before retrying to acquire the server lock. There are 5 retries in total.`

- Comment / default documentation.

**L0645** `# The wait time between retries is calculated as random(n, n + 500)`

- Comment / default documentation.

**L0646** `; oauth_refresh_token_server_lock_min_wait_ms = 1000`

- Comment / default documentation.

**L0647** ``

- Blank line.

**L0648** `# limit of api_key seconds to live before expiration`

- Comment / default documentation.

**L0649** `;api_key_max_seconds_to_live = -1`

- Comment / default documentation.

**L0650** ``

- Blank line.

**L0651** `# Set to true to enable SigV4 authentication option for HTTP-based datasources.`

- Comment / default documentation.

**L0652** `;sigv4_auth_enabled = false`

- Comment / default documentation.

**L0653** ``

- Blank line.

**L0654** `# Set to true to enable verbose logging of SigV4 request signing`

- Comment / default documentation.

**L0655** `;sigv4_verbose_logging = false`

- Comment / default documentation.

**L0656** ``

- Blank line.

**L0657** `# Set to true to enable Azure authentication option for HTTP-based datasources.`

- Comment / default documentation.

**L0658** `;azure_auth_enabled = false`

- Comment / default documentation.

**L0659** ``

- Blank line.

**L0660** `# Use email lookup in addition to the unique ID provided by the IdP`

- Comment / default documentation.

**L0661** `;oauth_allow_insecure_email_lookup = false`

- Comment / default documentation.

**L0662** ``

- Blank line.

**L0663** `# Set to true to include id of identity as a response header`

- Comment / default documentation.

**L0664** `;id_response_header_enabled = false`

- Comment / default documentation.

**L0665** ``

- Blank line.

**L0666** `# Prefix used for the id response header, X-Grafana-Identity-Id`

- Comment / default documentation.

**L0667** `;id_response_header_prefix = X-Grafana`

- Comment / default documentation.

**L0668** ``

- Blank line.

**L0669** `# List of identity namespaces to add id response headers for, separated by space.`

- Comment / default documentation.

**L0670** `# Available namespaces are user, api-key and service-account.`

- Comment / default documentation.

**L0671** `# The header value will encode the namespace ("user:<id>", "api-key:<id>", "service-account:<id>")`

- Comment / default documentation.

**L0672** `;id_response_header_namespaces = user api-key service-account`

- Comment / default documentation.

**L0673** ``

- Blank line.

**L0674** `# Enables the use of managed service accounts for plugin authentication`

- Comment / default documentation.

**L0675** `# This feature currently **only supports single-organization deployments**`

- Comment / default documentation.

**L0676** `; managed_service_accounts_enabled = false`

- Comment / default documentation.

**L0677** ``

- Blank line.

**L0678** `#################################### Anonymous Auth ######################`

- Comment / default documentation.

**L0679** `[auth.anonymous]`

- Section header: auth.anonymous

**L0680** `# enable anonymous access`

- Comment / default documentation.

**L0681** `;enabled = false`

- Comment / default documentation.

**L0682** ``

- Blank line.

**L0683** `# specify organization name that should be used for unauthenticated users`

- Comment / default documentation.

**L0684** `;org_name = Main Org.`

- Comment / default documentation.

**L0685** ``

- Blank line.

**L0686** `# specify role for unauthenticated users`

- Comment / default documentation.

**L0687** `;org_role = Viewer`

- Comment / default documentation.

**L0688** ``

- Blank line.

**L0689** `# mask the Grafana version number for unauthenticated users`

- Comment / default documentation.

**L0690** `;hide_version = false`

- Comment / default documentation.

**L0691** ``

- Blank line.

**L0692** `# number of devices in total`

- Comment / default documentation.

**L0693** `;device_limit =`

- Comment / default documentation.

**L0694** ``

- Blank line.

**L0695** `#################################### GitHub Auth ##########################`

- Comment / default documentation.

**L0696** `[auth.github]`

- Section header: auth.github

**L0697** `;name = GitHub`

- Comment / default documentation.

**L0698** `;icon = github`

- Comment / default documentation.

**L0699** `;enabled = false`

- Comment / default documentation.

**L0700** `;allow_sign_up = true`

- Comment / default documentation.

**L0701** `;auto_login = false`

- Comment / default documentation.

**L0702** `;client_id = some_id`

- Comment / default documentation.

**L0703** `;client_secret = some_secret`

- Comment / default documentation.

**L0704** `;scopes = user:email,read:org`

- Comment / default documentation.

**L0705** `;auth_url = https://github.com/login/oauth/authorize`

- Comment / default documentation.

**L0706** `;token_url = https://github.com/login/oauth/access_token`

- Comment / default documentation.

**L0707** `;api_url = https://api.github.com/user`

- Comment / default documentation.

**L0708** `;signout_redirect_url =`

- Comment / default documentation.

**L0709** `;allowed_domains =`

- Comment / default documentation.

**L0710** `;team_ids =`

- Comment / default documentation.

**L0711** `;allowed_organizations =`

- Comment / default documentation.

**L0712** `;role_attribute_path =`

- Comment / default documentation.

**L0713** `;role_attribute_strict = false`

- Comment / default documentation.

**L0714** `;org_mapping =`

- Comment / default documentation.

**L0715** `;allow_assign_grafana_admin = false`

- Comment / default documentation.

**L0716** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0717** `;tls_skip_verify_insecure = false`

- Comment / default documentation.

**L0718** `;tls_client_cert =`

- Comment / default documentation.

**L0719** `;tls_client_key =`

- Comment / default documentation.

**L0720** `;tls_client_ca =`

- Comment / default documentation.

**L0721** `# GitHub OAuth apps does not provide refresh tokens and the access tokens never expires.`

- Comment / default documentation.

**L0722** `;use_refresh_token = false`

- Comment / default documentation.

**L0723** ``

- Blank line.

**L0724** `#################################### GitLab Auth #########################`

- Comment / default documentation.

**L0725** `[auth.gitlab]`

- Section header: auth.gitlab

**L0726** `;name = GitLab`

- Comment / default documentation.

**L0727** `;icon = gitlab`

- Comment / default documentation.

**L0728** `;enabled = false`

- Comment / default documentation.

**L0729** `;allow_sign_up = true`

- Comment / default documentation.

**L0730** `;auto_login = false`

- Comment / default documentation.

**L0731** `;client_id = some_id`

- Comment / default documentation.

**L0732** `;client_secret = some_secret`

- Comment / default documentation.

**L0733** `;scopes = openid email profile`

- Comment / default documentation.

**L0734** `;auth_url = https://gitlab.com/oauth/authorize`

- Comment / default documentation.

**L0735** `;token_url = https://gitlab.com/oauth/token`

- Comment / default documentation.

**L0736** `;api_url = https://gitlab.com/api/v4`

- Comment / default documentation.

**L0737** `;signout_redirect_url =`

- Comment / default documentation.

**L0738** `;allowed_domains =`

- Comment / default documentation.

**L0739** `;allowed_groups =`

- Comment / default documentation.

**L0740** `;role_attribute_path =`

- Comment / default documentation.

**L0741** `;role_attribute_strict = false`

- Comment / default documentation.

**L0742** `;org_mapping =`

- Comment / default documentation.

**L0743** `;allow_assign_grafana_admin = false`

- Comment / default documentation.

**L0744** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0745** `;tls_skip_verify_insecure = false`

- Comment / default documentation.

**L0746** `;tls_client_cert =`

- Comment / default documentation.

**L0747** `;tls_client_key =`

- Comment / default documentation.

**L0748** `;tls_client_ca =`

- Comment / default documentation.

**L0749** `;use_pkce = true`

- Comment / default documentation.

**L0750** `;use_refresh_token = true`

- Comment / default documentation.

**L0751** ``

- Blank line.

**L0752** `#################################### Google Auth ##########################`

- Comment / default documentation.

**L0753** `[auth.google]`

- Section header: auth.google

**L0754** `;name = Google`

- Comment / default documentation.

**L0755** `;icon = google`

- Comment / default documentation.

**L0756** `;enabled = false`

- Comment / default documentation.

**L0757** `;allow_sign_up = true`

- Comment / default documentation.

**L0758** `;auto_login = false`

- Comment / default documentation.

**L0759** `;client_id = some_client_id`

- Comment / default documentation.

**L0760** `;client_secret = some_client_secret`

- Comment / default documentation.

**L0761** `;scopes = openid email profile`

- Comment / default documentation.

**L0762** `;auth_url = https://accounts.google.com/o/oauth2/v2/auth`

- Comment / default documentation.

**L0763** `;token_url = https://oauth2.googleapis.com/token`

- Comment / default documentation.

**L0764** `;api_url = https://openidconnect.googleapis.com/v1/userinfo`

- Comment / default documentation.

**L0765** `;signout_redirect_url =`

- Comment / default documentation.

**L0766** `;allowed_domains =`

- Comment / default documentation.

**L0767** `;validate_hd =`

- Comment / default documentation.

**L0768** `;hosted_domain =`

- Comment / default documentation.

**L0769** `;allowed_groups =`

- Comment / default documentation.

**L0770** `;role_attribute_path =`

- Comment / default documentation.

**L0771** `;role_attribute_strict = false`

- Comment / default documentation.

**L0772** `;org_mapping =`

- Comment / default documentation.

**L0773** `;allow_assign_grafana_admin = false`

- Comment / default documentation.

**L0774** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0775** `;tls_skip_verify_insecure = false`

- Comment / default documentation.

**L0776** `;tls_client_cert =`

- Comment / default documentation.

**L0777** `;tls_client_key =`

- Comment / default documentation.

**L0778** `;tls_client_ca =`

- Comment / default documentation.

**L0779** `;use_pkce = true`

- Comment / default documentation.

**L0780** `;use_refresh_token = true`

- Comment / default documentation.

**L0781** ``

- Blank line.

**L0782** `#################################### Grafana.com Auth ####################`

- Comment / default documentation.

**L0783** `[auth.grafana_com]`

- Section header: auth.grafana_com

**L0784** `;name = Grafana.com`

- Comment / default documentation.

**L0785** `;icon = grafana`

- Comment / default documentation.

**L0786** `;enabled = false`

- Comment / default documentation.

**L0787** `;allow_sign_up = true`

- Comment / default documentation.

**L0788** `;auto_login = false`

- Comment / default documentation.

**L0789** `;client_id = some_id`

- Comment / default documentation.

**L0790** `;client_secret = some_secret`

- Comment / default documentation.

**L0791** `;scopes = user:email`

- Comment / default documentation.

**L0792** `;allowed_organizations =`

- Comment / default documentation.

**L0793** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0794** `;use_refresh_token = false`

- Comment / default documentation.

**L0795** ``

- Blank line.

**L0796** `#################################### Azure AD OAuth #######################`

- Comment / default documentation.

**L0797** `[auth.azuread]`

- Section header: auth.azuread

**L0798** `;name = Microsoft`

- Comment / default documentation.

**L0799** `;icon = microsoft`

- Comment / default documentation.

**L0800** `;enabled = false`

- Comment / default documentation.

**L0801** `;allow_sign_up = true`

- Comment / default documentation.

**L0802** `;auto_login = false`

- Comment / default documentation.

**L0803** `;client_authentication =`

- Comment / default documentation.

**L0804** `;client_id = some_client_id`

- Comment / default documentation.

**L0805** `;client_secret = some_client_secret`

- Comment / default documentation.

**L0806** `;managed_identity_client_id =`

- Comment / default documentation.

**L0807** `;federated_credential_audience =`

- Comment / default documentation.

**L0808** `;workload_identity_token_file =`

- Comment / default documentation.

**L0809** `;scopes = openid email profile`

- Comment / default documentation.

**L0810** `;auth_url = https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/authorize`

- Comment / default documentation.

**L0811** `;token_url = https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token`

- Comment / default documentation.

**L0812** `;signout_redirect_url =`

- Comment / default documentation.

**L0813** `;allowed_domains =`

- Comment / default documentation.

**L0814** `;allowed_groups =`

- Comment / default documentation.

**L0815** `;allowed_organizations =`

- Comment / default documentation.

**L0816** `;role_attribute_strict = false`

- Comment / default documentation.

**L0817** `;org_mapping =`

- Comment / default documentation.

**L0818** `;allow_assign_grafana_admin = false`

- Comment / default documentation.

**L0819** `;use_pkce = true`

- Comment / default documentation.

**L0820** `# prevent synchronizing users organization roles`

- Comment / default documentation.

**L0821** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0822** `;use_refresh_token = true`

- Comment / default documentation.

**L0823** ``

- Blank line.

**L0824** `#################################### Okta OAuth #######################`

- Comment / default documentation.

**L0825** `[auth.okta]`

- Section header: auth.okta

**L0826** `;name = Okta`

- Comment / default documentation.

**L0827** `;enabled = false`

- Comment / default documentation.

**L0828** `;allow_sign_up = true`

- Comment / default documentation.

**L0829** `;auto_login = false`

- Comment / default documentation.

**L0830** `;client_id = some_id`

- Comment / default documentation.

**L0831** `;client_secret = some_secret`

- Comment / default documentation.

**L0832** `;scopes = openid profile email groups`

- Comment / default documentation.

**L0833** `;auth_url = https://<tenant-id>.okta.com/oauth2/v1/authorize`

- Comment / default documentation.

**L0834** `;token_url = https://<tenant-id>.okta.com/oauth2/v1/token`

- Comment / default documentation.

**L0835** `;api_url = https://<tenant-id>.okta.com/oauth2/v1/userinfo`

- Comment / default documentation.

**L0836** `;signout_redirect_url =`

- Comment / default documentation.

**L0837** `;allowed_domains =`

- Comment / default documentation.

**L0838** `;allowed_groups =`

- Comment / default documentation.

**L0839** `;role_attribute_path =`

- Comment / default documentation.

**L0840** `;role_attribute_strict = false`

- Comment / default documentation.

**L0841** `; org_attribute_path =`

- Comment / default documentation.

**L0842** `; org_mapping =`

- Comment / default documentation.

**L0843** `;allow_assign_grafana_admin = false`

- Comment / default documentation.

**L0844** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0845** `;tls_skip_verify_insecure = false`

- Comment / default documentation.

**L0846** `;tls_client_cert =`

- Comment / default documentation.

**L0847** `;tls_client_key =`

- Comment / default documentation.

**L0848** `;tls_client_ca =`

- Comment / default documentation.

**L0849** `;use_pkce = true`

- Comment / default documentation.

**L0850** `;use_refresh_token = true`

- Comment / default documentation.

**L0851** ``

- Blank line.

**L0852** `#################################### Generic OAuth ##########################`

- Comment / default documentation.

**L0853** `[auth.generic_oauth]`

- Section header: auth.generic_oauth

**L0854** `;name = OAuth`

- Comment / default documentation.

**L0855** `;icon = signin`

- Comment / default documentation.

**L0856** `;enabled = false`

- Comment / default documentation.

**L0857** `;allow_sign_up = true`

- Comment / default documentation.

**L0858** `;auto_login = false`

- Comment / default documentation.

**L0859** `;client_id = some_id`

- Comment / default documentation.

**L0860** `;client_secret = some_secret`

- Comment / default documentation.

**L0861** `;scopes = user:email,read:org`

- Comment / default documentation.

**L0862** `;empty_scopes = false`

- Comment / default documentation.

**L0863** `;email_attribute_name = email:primary`

- Comment / default documentation.

**L0864** `;email_attribute_path =`

- Comment / default documentation.

**L0865** `;login_attribute_path =`

- Comment / default documentation.

**L0866** `;name_attribute_path =`

- Comment / default documentation.

**L0867** `;role_attribute_path =`

- Comment / default documentation.

**L0868** `;role_attribute_strict = false`

- Comment / default documentation.

**L0869** `;groups_attribute_path =`

- Comment / default documentation.

**L0870** `;id_token_attribute_name =`

- Comment / default documentation.

**L0871** `;team_ids_attribute_path`

- Comment / default documentation.

**L0872** `;auth_url = https://foo.bar/login/oauth/authorize`

- Comment / default documentation.

**L0873** `;token_url = https://foo.bar/login/oauth/access_token`

- Comment / default documentation.

**L0874** `;api_url = https://foo.bar/user`

- Comment / default documentation.

**L0875** `;signout_redirect_url =`

- Comment / default documentation.

**L0876** `;teams_url =`

- Comment / default documentation.

**L0877** `;allowed_domains =`

- Comment / default documentation.

**L0878** `;team_ids =`

- Comment / default documentation.

**L0879** `;allowed_organizations =`

- Comment / default documentation.

**L0880** `;org_attribute_path =`

- Comment / default documentation.

**L0881** `;org_mapping =`

- Comment / default documentation.

**L0882** `;team_ids_attribute_path =`

- Comment / default documentation.

**L0883** `;tls_skip_verify_insecure = false`

- Comment / default documentation.

**L0884** `;tls_client_cert =`

- Comment / default documentation.

**L0885** `;tls_client_key =`

- Comment / default documentation.

**L0886** `;tls_client_ca =`

- Comment / default documentation.

**L0887** `;use_pkce = false`

- Comment / default documentation.

**L0888** `;auth_style =`

- Comment / default documentation.

**L0889** `;allow_assign_grafana_admin = false`

- Comment / default documentation.

**L0890** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0891** `;use_refresh_token = false`

- Comment / default documentation.

**L0892** ``

- Blank line.

**L0893** `#################################### Basic Auth ##########################`

- Comment / default documentation.

**L0894** `[auth.basic]`

- Section header: auth.basic

**L0895** `;enabled = true`

- Comment / default documentation.

**L0896** `;password_policy = false`

- Comment / default documentation.

**L0897** ``

- Blank line.

**L0898** `#################################### Auth Proxy ##########################`

- Comment / default documentation.

**L0899** `[auth.proxy]`

- Section header: auth.proxy

**L0900** `;enabled = false`

- Comment / default documentation.

**L0901** `;header_name = X-WEBAUTH-USER`

- Comment / default documentation.

**L0902** `;header_property = username`

- Comment / default documentation.

**L0903** `;auto_sign_up = true`

- Comment / default documentation.

**L0904** `;sync_ttl = 60`

- Comment / default documentation.

**L0905** `;whitelist = 192.168.1.1, 192.168.2.1`

- Comment / default documentation.

**L0906** `;headers = Email:X-User-Email, Name:X-User-Name`

- Comment / default documentation.

**L0907** `# Non-ASCII strings in header values are encoded using quoted-printable encoding`

- Comment / default documentation.

**L0908** `;headers_encoded = false`

- Comment / default documentation.

**L0909** `# Read the auth proxy docs for details on what the setting below enables`

- Comment / default documentation.

**L0910** `;enable_login_token = false`

- Comment / default documentation.

**L0911** ``

- Blank line.

**L0912** `#################################### Auth JWT ##########################`

- Comment / default documentation.

**L0913** `[auth.jwt]`

- Section header: auth.jwt

**L0914** `;enabled = true`

- Comment / default documentation.

**L0915** `;enable_login_token = false`

- Comment / default documentation.

**L0916** `;header_name = X-JWT-Assertion`

- Comment / default documentation.

**L0917** `;email_claim = sub`

- Comment / default documentation.

**L0918** `;username_claim = sub`

- Comment / default documentation.

**L0919** `;email_attribute_path = jmespath.email`

- Comment / default documentation.

**L0920** `;username_attribute_path = jmespath.username`

- Comment / default documentation.

**L0921** `;jwk_set_url = https://foo.bar/.well-known/jwks.json`

- Comment / default documentation.

**L0922** `;jwk_set_bearer_token_file = /path/to/token/file`

- Comment / default documentation.

**L0923** `;jwk_set_file = /path/to/jwks.json`

- Comment / default documentation.

**L0924** `;cache_ttl = 60m`

- Comment / default documentation.

**L0925** `;expect_claims = {"aud": ["foo", "bar"]}`

- Comment / default documentation.

**L0926** `;key_file = /path/to/key/file`

- Comment / default documentation.

**L0927** `# Use in conjunction with key_file in case the JWT token's header specifies a key ID in "kid" field`

- Comment / default documentation.

**L0928** `;key_id = some-key-id`

- Comment / default documentation.

**L0929** `;role_attribute_path =`

- Comment / default documentation.

**L0930** `;role_attribute_strict = false`

- Comment / default documentation.

**L0931** `;org_attribute_path =`

- Comment / default documentation.

**L0932** `;org_mapping =`

- Comment / default documentation.

**L0933** `;groups_attribute_path =`

- Comment / default documentation.

**L0934** `;auto_sign_up = false`

- Comment / default documentation.

**L0935** `;url_login = false`

- Comment / default documentation.

**L0936** `;allow_assign_grafana_admin = false`

- Comment / default documentation.

**L0937** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0938** `;signout_redirect_url =`

- Comment / default documentation.

**L0939** `;tls_client_ca =`

- Comment / default documentation.

**L0940** `;tls_skip_verify_insecure = false`

- Comment / default documentation.

**L0941** ``

- Blank line.

**L0942** `#################################### Auth LDAP ##########################`

- Comment / default documentation.

**L0943** `[auth.ldap]`

- Section header: auth.ldap

**L0944** `;enabled = false`

- Comment / default documentation.

**L0945** `;config_file = /etc/grafana/ldap.toml`

- Comment / default documentation.

**L0946** `;allow_sign_up = true`

- Comment / default documentation.

**L0947** `# prevent synchronizing ldap users organization roles`

- Comment / default documentation.

**L0948** `;skip_org_role_sync = false`

- Comment / default documentation.

**L0949** ``

- Blank line.

**L0950** `# LDAP background sync (Enterprise only)`

- Comment / default documentation.

**L0951** `# At 1 am every day`

- Comment / default documentation.

**L0952** `;sync_cron = "0 1 * * *"`

- Comment / default documentation.

**L0953** `;active_sync_enabled = true`

- Comment / default documentation.

**L0954** ``

- Blank line.

**L0955** `#################################### AWS ###########################`

- Comment / default documentation.

**L0956** `[aws]`

- Section header: aws

**L0957** `# Enter a comma-separated list of allowed AWS authentication providers.`

- Comment / default documentation.

**L0958** `# Options are: default (AWS SDK Default), keys (Access && secret key), credentials (Credentials field), ec2_iam_role (EC2 IAM Role)`

- Comment / default documentation.

**L0959** `; allowed_auth_providers = default,keys,credentials`

- Comment / default documentation.

**L0960** ``

- Blank line.

**L0961** `# Allow AWS users to assume a role using temporary security credentials.`

- Comment / default documentation.

**L0962** `# If true, assume role will be enabled for all AWS authentication providers that are specified in aws_auth_providers`

- Comment / default documentation.

**L0963** `; assume_role_enabled = true`

- Comment / default documentation.

**L0964** ``

- Blank line.

**L0965** `# Specify max no of pages to be returned by the ListMetricPages API`

- Comment / default documentation.

**L0966** `; list_metrics_page_limit = 500`

- Comment / default documentation.

**L0967** ``

- Blank line.

**L0968** `# Experimental, for use in Grafana Cloud only. Please do not set.`

- Comment / default documentation.

**L0969** `; external_id =`

- Comment / default documentation.

**L0970** ``

- Blank line.

**L0971** `# Sets the expiry duration of an assumed role.`

- Comment / default documentation.

**L0972** `# This setting should be expressed as a duration. Examples: 6h (hours), 10d (days), 2w (weeks), 1M (month).`

- Comment / default documentation.

**L0973** `; session_duration = "15m"`

- Comment / default documentation.

**L0974** ``

- Blank line.

**L0975** `# Set the plugins that will receive AWS settings for each request (via plugin context)`

- Comment / default documentation.

**L0976** `# By default this will include all Grafana Labs owned AWS plugins, or those that make use of AWS settings (ElasticSearch, Prometheus).`

- Comment / default documentation.

**L0977** `; forward_settings_to_plugins = cloudwatch, grafana-athena-datasource, grafana-redshift-datasource, grafana-x-ray-datasource, grafana-timestream-datasource, grafana-iot-sitewise-datasource, grafana-iot-twinmaker-app, grafana-opensearch-datasource, aws-datasource-provisioner, elasticsearch, prometheus`

- Comment / default documentation.

**L0978** ``

- Blank line.

**L0979** `#################################### Azure ###############################`

- Comment / default documentation.

**L0980** `[azure]`

- Section header: azure

**L0981** `# Azure cloud environment where Grafana is hosted`

- Comment / default documentation.

**L0982** `# Possible values are AzureCloud, AzureChinaCloud, AzureUSGovernment and AzureGermanCloud`

- Comment / default documentation.

**L0983** `# Default value is AzureCloud (i.e. public cloud)`

- Comment / default documentation.

**L0984** `;cloud = AzureCloud`

- Comment / default documentation.

**L0985** ``

- Blank line.

**L0986** `# A customized list of Azure cloud settings and properties, used by data sources which need this information when run in non-standard azure environments`

- Comment / default documentation.

**L0987** `# When specified, this list will replace the default cloud list of AzureCloud, AzureChinaCloud, AzureUSGovernment and AzureGermanCloud`

- Comment / default documentation.

**L0988** `;clouds_config = \`[`

- Comment / default documentation.

**L0989** `;		{`

- Comment / default documentation.

**L0990** `;			"name":"CustomCloud1",`

- Comment / default documentation.

**L0991** `;			"displayName":"Custom Cloud 1",`

- Comment / default documentation.

**L0992** `;			"aadAuthority":"https://login.cloud1.contoso.com/",`

- Comment / default documentation.

**L0993** `;			"properties":{`

- Comment / default documentation.

**L0994** `;				"azureDataExplorerSuffix": ".kusto.windows.cloud1.contoso.com",`

- Comment / default documentation.

**L0995** `;				"logAnalytics":            "https://api.loganalytics.cloud1.contoso.com",`

- Comment / default documentation.

**L0996** `;				"portal":                  "https://portal.azure.cloud1.contoso.com",`

- Comment / default documentation.

**L0997** `;				"prometheusResourceId":    "https://prometheus.monitor.azure.cloud1.contoso.com",`

- Comment / default documentation.

**L0998** `;				"resourceManager":         "https://management.azure.cloud1.contoso.com"`

- Comment / default documentation.

**L0999** `;			}`

- Comment / default documentation.

**L1000** `;		}]\``

- Comment / default documentation.

**L1001** ``

- Blank line.

**L1002** `# Specifies whether Grafana hosted in Azure service with Managed Identity configured (e.g. Azure Virtual Machines instance)`

- Comment / default documentation.

**L1003** `# If enabled, the managed identity can be used for authentication of Grafana in Azure services`

- Comment / default documentation.

**L1004** `# Disabled by default, needs to be explicitly enabled`

- Comment / default documentation.

**L1005** `;managed_identity_enabled = false`

- Comment / default documentation.

**L1006** ``

- Blank line.

**L1007** `# Client ID to use for user-assigned managed identity`

- Comment / default documentation.

**L1008** `# Should be set for user-assigned identity and should be empty for system-assigned identity`

- Comment / default documentation.

**L1009** `;managed_identity_client_id =`

- Comment / default documentation.

**L1010** ``

- Blank line.

**L1011** `# Specifies whether Azure AD Workload Identity authentication should be enabled in datasources that support it`

- Comment / default documentation.

**L1012** `# For more documentation on Azure AD Workload Identity, review this documentation:`

- Comment / default documentation.

**L1013** `# https://azure.github.io/azure-workload-identity/docs/`

- Comment / default documentation.

**L1014** `# Disabled by default, needs to be explicitly enabled`

- Comment / default documentation.

**L1015** `;workload_identity_enabled = false`

- Comment / default documentation.

**L1016** ``

- Blank line.

**L1017** `# Tenant ID of the Azure AD Workload Identity`

- Comment / default documentation.

**L1018** `# Allows to override default tenant ID of the Azure AD identity associated with the Kubernetes service account`

- Comment / default documentation.

**L1019** `;workload_identity_tenant_id =`

- Comment / default documentation.

**L1020** ``

- Blank line.

**L1021** `# Client ID of the Azure AD Workload Identity`

- Comment / default documentation.

**L1022** `# Allows to override default client ID of the Azure AD identity associated with the Kubernetes service account`

- Comment / default documentation.

**L1023** `;workload_identity_client_id =`

- Comment / default documentation.

**L1024** ``

- Blank line.

**L1025** `# Custom path to token file for the Azure AD Workload Identity`

- Comment / default documentation.

**L1026** `# Allows to set a custom path to the projected service account token file`

- Comment / default documentation.

**L1027** `;workload_identity_token_file =`

- Comment / default documentation.

**L1028** ``

- Blank line.

**L1029** `# Specifies whether user identity authentication (on behalf of currently signed-in user) should be enabled in datasources`

- Comment / default documentation.

**L1030** `# that support it (requires AAD authentication)`

- Comment / default documentation.

**L1031** `# Disabled by default, needs to be explicitly enabled`

- Comment / default documentation.

**L1032** `;user_identity_enabled = false`

- Comment / default documentation.

**L1033** ``

- Blank line.

**L1034** `# Specifies whether user identity authentication fallback credentials should be enabled in data sources`

- Comment / default documentation.

**L1035** `# Enabling this allows data source creators to provide fallback credentials for backend initiated requests`

- Comment / default documentation.

**L1036** `# e.g. alerting, recorded queries etc.`

- Comment / default documentation.

**L1037** `# Enabled by default, needs to be explicitly disabled`

- Comment / default documentation.

**L1038** `# Will not have any effect if user identity is disabled above`

- Comment / default documentation.

**L1039** `;user_identity_fallback_credentials_enabled = true`

- Comment / default documentation.

**L1040** ``

- Blank line.

**L1041** `# Override token URL for Azure Active Directory`

- Comment / default documentation.

**L1042** `# By default is the same as token URL configured for AAD authentication settings`

- Comment / default documentation.

**L1043** `;user_identity_token_url =`

- Comment / default documentation.

**L1044** ``

- Blank line.

**L1045** `# Override client authentication method for Azure Active Directory`

- Comment / default documentation.

**L1046** `# By default is the same as client authentication method configured for AAD authentication settings`

- Comment / default documentation.

**L1047** `;user_identity_client_authentication =`

- Comment / default documentation.

**L1048** ``

- Blank line.

**L1049** `# Override ADD application ID which would be used to exchange users token to an access token for the datasource`

- Comment / default documentation.

**L1050** `# By default is the same as used in AAD authentication or can be set to another application (for OBO flow)`

- Comment / default documentation.

**L1051** `;user_identity_client_id =`

- Comment / default documentation.

**L1052** ``

- Blank line.

**L1053** `# Override the AAD application client secret`

- Comment / default documentation.

**L1054** `# By default is the same as used in AAD authentication or can be set to another application (for OBO flow)`

- Comment / default documentation.

**L1055** `;user_identity_client_secret =`

- Comment / default documentation.

**L1056** ``

- Blank line.

**L1057** `# Override the AAD managed identity client ID`

- Comment / default documentation.

**L1058** `# By default is the same as used in AAD authentication or can be set to another managed identity (for OBO flow)`

- Comment / default documentation.

**L1059** `;user_identity_managed_identity_client_id =`

- Comment / default documentation.

**L1060** ``

- Blank line.

**L1061** `# Override the AAD federated credential audience`

- Comment / default documentation.

**L1062** `# By default is the same as used in AAD authentication or can be set to another audience (for OBO flow)`

- Comment / default documentation.

**L1063** `;user_identity_federated_credential_audience =`

- Comment / default documentation.

**L1064** ``

- Blank line.

**L1065** `# Allows the usage of a custom token request assertion when Grafana is behind an authentication proxy`

- Comment / default documentation.

**L1066** `# In most cases this will not need to be used. To enable this set the value to "username"`

- Comment / default documentation.

**L1067** `# The default is empty and any other value will not enable this functionality`

- Comment / default documentation.

**L1068** `;username_assertion =`

- Comment / default documentation.

**L1069** ``

- Blank line.

**L1070** `# Set the plugins that will receive Azure settings for each request (via plugin context)`

- Comment / default documentation.

**L1071** `# By default this will include all Grafana Labs owned Azure plugins, or those that make use of Azure settings (Azure Monitor, Azure Data Explorer, Prometheus, MSSQL).`

- Comment / default documentation.

**L1072** `;forward_settings_to_plugins = grafana-azure-monitor-datasource, prometheus, grafana-azure-data-explorer-datasource, mssql, grafana-azureprometheus-datasourc`

- Comment / default documentation.

**L1073** ``

- Blank line.

**L1074** `# Specifies whether Entra password auth can be used for the MSSQL data source`

- Comment / default documentation.

**L1075** `# Disabled by default, needs to be explicitly enabled`

- Comment / default documentation.

**L1076** `;azure_entra_password_credentials_enabled = false`

- Comment / default documentation.

**L1077** ``

- Blank line.

**L1078** `#################################### Role-based Access Control ###########`

- Comment / default documentation.

**L1079** `[rbac]`

- Section header: rbac

**L1080** `;permission_cache = true`

- Comment / default documentation.

**L1081** ``

- Blank line.

**L1082** `# Reset basic roles permissions on boot`

- Comment / default documentation.

**L1083** `# Warning left to true, basic roles permissions will be reset on every boot`

- Comment / default documentation.

**L1084** `#reset_basic_roles = false`

- Comment / default documentation.

**L1085** ``

- Blank line.

**L1086** `# Validate permissions' action and scope on role creation and update`

- Comment / default documentation.

**L1087** `; permission_validation_enabled = true`

- Comment / default documentation.

**L1088** ``

- Blank line.

**L1089** `#################################### SMTP / Emailing ##########################`

- Comment / default documentation.

**L1090** `[smtp]`

- Section header: smtp

**L1091** `;enabled = false`

- Comment / default documentation.

**L1092** `;host = localhost:25`

- Comment / default documentation.

**L1093** `;user =`

- Comment / default documentation.

**L1094** `# If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""`

- Comment / default documentation.

**L1095** `;password =`

- Comment / default documentation.

**L1096** `;cert_file =`

- Comment / default documentation.

**L1097** `;key_file =`

- Comment / default documentation.

**L1098** `;skip_verify = false`

- Comment / default documentation.

**L1099** `;from_address = admin@grafana.localhost`

- Comment / default documentation.

**L1100** `;from_name = Grafana`

- Comment / default documentation.

**L1101** `# EHLO identity in SMTP dialog (defaults to instance_name)`

- Comment / default documentation.

**L1102** `;ehlo_identity = dashboard.example.com`

- Comment / default documentation.

**L1103** `# SMTP startTLS policy (defaults to 'OpportunisticStartTLS')`

- Comment / default documentation.

**L1104** `;startTLS_policy = NoStartTLS`

- Comment / default documentation.

**L1105** `# Enable trace propagation in e-mail headers, using the 'traceparent', 'tracestate' and (optionally) 'baggage' fields (defaults to false)`

- Comment / default documentation.

**L1106** `;enable_tracing = false`

- Comment / default documentation.

**L1107** ``

- Blank line.

**L1108** `[smtp.static_headers]`

- Section header: smtp.static_headers

**L1109** `# Include custom static headers in all outgoing emails`

- Comment / default documentation.

**L1110** `;Foo-Header = bar`

- Comment / default documentation.

**L1111** `;Foo = bar`

- Comment / default documentation.

**L1112** ``

- Blank line.

**L1113** `[emails]`

- Section header: emails

**L1114** `;welcome_email_on_sign_up = false`

- Comment / default documentation.

**L1115** `;templates_pattern = emails/*.html, emails/*.txt`

- Comment / default documentation.

**L1116** `;content_types = text/html`

- Comment / default documentation.

**L1117** ``

- Blank line.

**L1118** `#################################### Logging ##########################`

- Comment / default documentation.

**L1119** `[log]`

- Section header: log

**L1120** `# Either "console", "file", "syslog". Default is console and  file`

- Comment / default documentation.

**L1121** `# Use space to separate multiple modes, e.g. "console file"`

- Comment / default documentation.

**L1122** `;mode = console file`

- Comment / default documentation.

**L1123** ``

- Blank line.

**L1124** `# Either "debug", "info", "warn", "error". Default is "info"`

- Comment / default documentation.

**L1125** `;level = info`

- Comment / default documentation.

**L1126** ``

- Blank line.

**L1127** `# optional settings to set different levels for specific loggers. Ex filters = sqlstore:debug`

- Comment / default documentation.

**L1128** `;filters =`

- Comment / default documentation.

**L1129** ``

- Blank line.

**L1130** `# Set the default error message shown to users. This message is displayed instead of sensitive backend errors which should be obfuscated. Default is the same as the sample value.`

- Comment / default documentation.

**L1131** `;user_facing_default_error = "please inspect Grafana server log for details"`

- Comment / default documentation.

**L1132** ``

- Blank line.

**L1133** `# For "console" mode only`

- Comment / default documentation.

**L1134** `[log.console]`

- Section header: log.console

**L1135** `;level =`

- Comment / default documentation.

**L1136** ``

- Blank line.

**L1137** `# log line format, valid options are text, console and json`

- Comment / default documentation.

**L1138** `;format = console`

- Comment / default documentation.

**L1139** ``

- Blank line.

**L1140** `# For "file" mode only`

- Comment / default documentation.

**L1141** `[log.file]`

- Section header: log.file

**L1142** `;level =`

- Comment / default documentation.

**L1143** ``

- Blank line.

**L1144** `# log line format, valid options are text, console and json`

- Comment / default documentation.

**L1145** `;format = text`

- Comment / default documentation.

**L1146** ``

- Blank line.

**L1147** `# This enables automated log rotate(switch of following options), default is true`

- Comment / default documentation.

**L1148** `;log_rotate = true`

- Comment / default documentation.

**L1149** ``

- Blank line.

**L1150** `# Max line number of single file, default is 1000000`

- Comment / default documentation.

**L1151** `;max_lines = 1000000`

- Comment / default documentation.

**L1152** ``

- Blank line.

**L1153** `# Max size shift of single file, default is 28 means 1 << 28, 256MB`

- Comment / default documentation.

**L1154** `;max_size_shift = 28`

- Comment / default documentation.

**L1155** ``

- Blank line.

**L1156** `# Segment log daily, default is true`

- Comment / default documentation.

**L1157** `;daily_rotate = true`

- Comment / default documentation.

**L1158** ``

- Blank line.

**L1159** `# Expired days of log file(delete after max days), default is 7`

- Comment / default documentation.

**L1160** `;max_days = 7`

- Comment / default documentation.

**L1161** ``

- Blank line.

**L1162** `[log.syslog]`

- Section header: log.syslog

**L1163** `;level =`

- Comment / default documentation.

**L1164** ``

- Blank line.

**L1165** `# log line format, valid options are text, console and json`

- Comment / default documentation.

**L1166** `;format = text`

- Comment / default documentation.

**L1167** ``

- Blank line.

**L1168** `# Syslog network type and address. This can be udp, tcp, or unix. If left blank, the default unix endpoints will be used.`

- Comment / default documentation.

**L1169** `;network =`

- Comment / default documentation.

**L1170** `;address =`

- Comment / default documentation.

**L1171** ``

- Blank line.

**L1172** `# Syslog facility. user, daemon and local0 through local7 are valid.`

- Comment / default documentation.

**L1173** `;facility =`

- Comment / default documentation.

**L1174** ``

- Blank line.

**L1175** `# Syslog tag. By default, the process' argv[0] is used.`

- Comment / default documentation.

**L1176** `;tag =`

- Comment / default documentation.

**L1177** ``

- Blank line.

**L1178** `[log.frontend]`

- Section header: log.frontend

**L1179** `# Enables the Grafana Faro javascript agent integration for capturing frontend performance and error events.`

- Comment / default documentation.

**L1180** `;enabled = false`

- Comment / default documentation.

**L1181** ``

- Blank line.

**L1182** `# Custom HTTP endpoint to send Grafana Faro events to. Default will send events to /log-grafana-javascript-agent and log the events to stdout.`

- Comment / default documentation.

**L1183** `;custom_endpoint = /log-grafana-javascript-agent`

- Comment / default documentation.

**L1184** ``

- Blank line.

**L1185** `# API Key for Grafana Faro custom endpoint`

- Comment / default documentation.

**L1186** `;api_key =`

- Comment / default documentation.

**L1187** ``

- Blank line.

**L1188** `# level of internal logging for debugging Grafana Javascript Agent.`

- Comment / default documentation.

**L1189** `# possible values are: 0 = OFF, 1 = ERROR, 2 = WARN, 3 = INFO, 4 = VERBOSE`

- Comment / default documentation.

**L1190** `# more details: https://github.com/grafana/faro-web-sdk/blob/v1.3.7/docs/sources/tutorials/quick-start-browser.md#how-to-activate-debugging`

- Comment / default documentation.

**L1191** `;internal_logger_level =`

- Comment / default documentation.

**L1192** ``

- Blank line.

**L1193** `# Enables the Console instrumentation for Grafana Faro`

- Comment / default documentation.

**L1194** `# See https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/console-instrumentation/`

- Comment / default documentation.

**L1195** `;instrumentations_console_enabled = true`

- Comment / default documentation.

**L1196** ``

- Blank line.

**L1197** `# Enables the Performance instrumentation for Grafana Faro.`

- Comment / default documentation.

**L1198** `# See https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/performance-instrumentation/`

- Comment / default documentation.

**L1199** `;instrumentations_performance_enabled = true`

- Comment / default documentation.

**L1200** ``

- Blank line.

**L1201** `# Enables the Content Security Policy Violations instrumentation for Grafana Faro.`

- Comment / default documentation.

**L1202** `# See https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/csp-violation-tracking/`

- Comment / default documentation.

**L1203** `; instrumentations_csp_enabled = true`

- Comment / default documentation.

**L1204** ``

- Blank line.

**L1205** `# Enables the Tracing instrumentation for Grafana Faro.`

- Comment / default documentation.

**L1206** `# See https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/tracing-instrumentation/`

- Comment / default documentation.

**L1207** `;instrumentations_tracing_enabled = true`

- Comment / default documentation.

**L1208** ``

- Blank line.

**L1209** `# Enables sending attribution data for web vitals with the Performance instrumentation.`

- Comment / default documentation.

**L1210** `# See https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/web-vitals/#web-vitals-attribution-data`

- Comment / default documentation.

**L1211** `;web_vitals_attribution_enabled = true`

- Comment / default documentation.

**L1212** ``

- Blank line.

**L1213** `# Enables the bot filter for the Grafana Faro JavaScript agent integration. Default is \`false\`. When enabled, it will filter out requests from known bots and crawlers.`

- Comment / default documentation.

**L1214** `;bot_filter_enabled = false`

- Comment / default documentation.

**L1215** ``

- Blank line.

**L1216** `#################################### Usage Quotas ########################`

- Comment / default documentation.

**L1217** `[quota]`

- Section header: quota

**L1218** `; enabled = false`

- Comment / default documentation.

**L1219** ``

- Blank line.

**L1220** `#### set quotas to -1 to make unlimited. ####`

- Comment / default documentation.

**L1221** `# limit number of users per Org.`

- Comment / default documentation.

**L1222** `; org_user = 10`

- Comment / default documentation.

**L1223** ``

- Blank line.

**L1224** `# limit number of dashboards per Org.`

- Comment / default documentation.

**L1225** `; org_dashboard = 100`

- Comment / default documentation.

**L1226** ``

- Blank line.

**L1227** `# limit number of data_sources per Org.`

- Comment / default documentation.

**L1228** `; org_data_source = 10`

- Comment / default documentation.

**L1229** ``

- Blank line.

**L1230** `# limit number of api_keys per Org.`

- Comment / default documentation.

**L1231** `; org_api_key = 10`

- Comment / default documentation.

**L1232** ``

- Blank line.

**L1233** `# limit number of alerts per Org.`

- Comment / default documentation.

**L1234** `;org_alert_rule = 100`

- Comment / default documentation.

**L1235** ``

- Blank line.

**L1236** `# limit number of orgs a user can create.`

- Comment / default documentation.

**L1237** `; user_org = 10`

- Comment / default documentation.

**L1238** ``

- Blank line.

**L1239** `# Global limit of users.`

- Comment / default documentation.

**L1240** `; global_user = -1`

- Comment / default documentation.

**L1241** ``

- Blank line.

**L1242** `# global limit of orgs.`

- Comment / default documentation.

**L1243** `; global_org = -1`

- Comment / default documentation.

**L1244** ``

- Blank line.

**L1245** `# global limit of dashboards`

- Comment / default documentation.

**L1246** `; global_dashboard = -1`

- Comment / default documentation.

**L1247** ``

- Blank line.

**L1248** `# global limit of api_keys`

- Comment / default documentation.

**L1249** `; global_api_key = -1`

- Comment / default documentation.

**L1250** ``

- Blank line.

**L1251** `# global limit on number of logged in users.`

- Comment / default documentation.

**L1252** `; global_session = -1`

- Comment / default documentation.

**L1253** ``

- Blank line.

**L1254** `# global limit of alerts`

- Comment / default documentation.

**L1255** `;global_alert_rule = -1`

- Comment / default documentation.

**L1256** ``

- Blank line.

**L1257** `# global limit of files uploaded to the SQL DB`

- Comment / default documentation.

**L1258** `;global_file = 1000`

- Comment / default documentation.

**L1259** ``

- Blank line.

**L1260** `# global limit of correlations`

- Comment / default documentation.

**L1261** `; global_correlations = -1`

- Comment / default documentation.

**L1262** ``

- Blank line.

**L1263** `# Limit of the number of alert rules per rule group.`

- Comment / default documentation.

**L1264** `# This is not strictly enforced yet, but will be enforced over time.`

- Comment / default documentation.

**L1265** `;alerting_rule_group_rules = 100`

- Comment / default documentation.

**L1266** ``

- Blank line.

**L1267** `# Limit the number of query evaluation results per alert rule.`

- Comment / default documentation.

**L1268** `# If the condition query of an alert rule produces more results than this limit,`

- Comment / default documentation.

**L1269** `# the evaluation results in an error.`

- Comment / default documentation.

**L1270** `;alerting_rule_evaluation_results = -1`

- Comment / default documentation.

**L1271** ``

- Blank line.

**L1272** `#################################### Unified Alerting ####################`

- Comment / default documentation.

**L1273** `[unified_alerting]`

- Section header: unified_alerting

**L1274** `#Enable the Unified Alerting sub-system and interface. When enabled we'll migrate all of your alert rules and notification channels to the new system. New alert rules will be created and your notification channels will be converted into an Alertmanager configuration. Previous data is preserved to enable backwards compatibility but new data is removed.\`\`\``

- Comment / default documentation.

**L1275** `;enabled = true`

- Comment / default documentation.

**L1276** ``

- Blank line.

**L1277** `# Comma-separated list of organization IDs for which to disable unified alerting. Only supported if unified alerting is enabled.`

- Comment / default documentation.

**L1278** `;disabled_orgs =`

- Comment / default documentation.

**L1279** ``

- Blank line.

**L1280** `# Specify how long to wait for the alerting service to initialize`

- Comment / default documentation.

**L1281** `;initialization_timeout = 30s`

- Comment / default documentation.

**L1282** ``

- Blank line.

**L1283** `# Specify the frequency of polling for admin config changes.`

- Comment / default documentation.

**L1284** `# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1285** `;admin_config_poll_interval = 60s`

- Comment / default documentation.

**L1286** ``

- Blank line.

**L1287** `# Specify the frequency of polling for Alertmanager config changes.`

- Comment / default documentation.

**L1288** `# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1289** `;alertmanager_config_poll_interval = 60s`

- Comment / default documentation.

**L1290** ``

- Blank line.

**L1291** `# Maximum number of active and pending silences that a tenant can have at once. Default: 0 (no limit).`

- Comment / default documentation.

**L1292** `;alertmanager_max_silences_count =`

- Comment / default documentation.

**L1293** ``

- Blank line.

**L1294** `# Maximum silence size in bytes. Default: 0 (no limit).`

- Comment / default documentation.

**L1295** `;alertmanager_max_silence_size_bytes =`

- Comment / default documentation.

**L1296** ``

- Blank line.

**L1297** `# Redis server address or addresses. It can be a single Redis address if using Redis standalone,`

- Comment / default documentation.

**L1298** `# or a list of comma-separated addresses if using Redis Cluster/Sentinel.`

- Comment / default documentation.

**L1299** `;ha_redis_address =`

- Comment / default documentation.

**L1300** ``

- Blank line.

**L1301** `# Set to true when using Redis in Cluster mode. Mutually exclusive with ha_redis_sentinel_mode_enabled.`

- Comment / default documentation.

**L1302** `;ha_redis_cluster_mode_enabled = false`

- Comment / default documentation.

**L1303** ``

- Blank line.

**L1304** `# Set to true when using Redis in Sentinel mode. Mutually exclusive with ha_redis_cluster_mode_enabled.`

- Comment / default documentation.

**L1305** `;ha_redis_sentinel_mode_enabled = false`

- Comment / default documentation.

**L1306** ``

- Blank line.

**L1307** `# Redis Sentinel master name. Only applicable when ha_redis_sentinel_mode_enabled is set to true.`

- Comment / default documentation.

**L1308** `;ha_redis_sentinel_master_name =`

- Comment / default documentation.

**L1309** ``

- Blank line.

**L1310** `# The username that should be used to authenticate with Redis.`

- Comment / default documentation.

**L1311** `;ha_redis_username =`

- Comment / default documentation.

**L1312** ``

- Blank line.

**L1313** `# The password that should be used to authenticate with Redis.`

- Comment / default documentation.

**L1314** `;ha_redis_password =`

- Comment / default documentation.

**L1315** ``

- Blank line.

**L1316** `# The username that should be used to authenticate with Redis Sentinel.`

- Comment / default documentation.

**L1317** `# Only applicable when ha_redis_sentinel_mode_enabled is set to true.`

- Comment / default documentation.

**L1318** `;ha_redis_sentinel_username =`

- Comment / default documentation.

**L1319** ``

- Blank line.

**L1320** `# The password that should be used to authenticate with Redis Sentinel.`

- Comment / default documentation.

**L1321** `# Only applicable when ha_redis_sentinel_mode_enabled is set to true.`

- Comment / default documentation.

**L1322** `;ha_redis_sentinel_password =`

- Comment / default documentation.

**L1323** ``

- Blank line.

**L1324** `# The Redis database. The default value is 0.`

- Comment / default documentation.

**L1325** `;ha_redis_db =`

- Comment / default documentation.

**L1326** ``

- Blank line.

**L1327** `# A prefix that is used for every key or channel that is created on the Redis server as part of HA for alerting.`

- Comment / default documentation.

**L1328** `# Useful if you plan to share Redis with multiple Grafana instances.`

- Comment / default documentation.

**L1329** `;ha_redis_prefix =`

- Comment / default documentation.

**L1330** ``

- Blank line.

**L1331** `# The name of the cluster peer to use as an identifier. If none is provided, a random one is generated.`

- Comment / default documentation.

**L1332** `;ha_redis_peer_name =`

- Comment / default documentation.

**L1333** ``

- Blank line.

**L1334** `# The maximum number of simultaneous Redis connections.`

- Comment / default documentation.

**L1335** `;ha_redis_max_conns = 5`

- Comment / default documentation.

**L1336** ``

- Blank line.

**L1337** `# Enable TLS on the client used to communicate with the Redis server. This should be set to true`

- Comment / default documentation.

**L1338** `# if using any of the other ha_redis_tls_* fields.`

- Comment / default documentation.

**L1339** `;ha_redis_tls_enabled = false`

- Comment / default documentation.

**L1340** ``

- Blank line.

**L1341** `# Path to the PEM-encoded TLS client certificate file used to authenticate with the Redis server.`

- Comment / default documentation.

**L1342** `# Required if using Mutual TLS.`

- Comment / default documentation.

**L1343** `;ha_redis_tls_cert_path =`

- Comment / default documentation.

**L1344** ``

- Blank line.

**L1345** `# Path to the PEM-encoded TLS private key file. Also requires the client certificate to be configured.`

- Comment / default documentation.

**L1346** `# Required if using Mutual TLS.`

- Comment / default documentation.

**L1347** `;ha_redis_tls_key_path =`

- Comment / default documentation.

**L1348** ``

- Blank line.

**L1349** `# Path to the PEM-encoded CA certificates file. If not set, the host's root CA certificates are used.`

- Comment / default documentation.

**L1350** `;ha_redis_tls_ca_path =`

- Comment / default documentation.

**L1351** ``

- Blank line.

**L1352** `# Overrides the expected name of the Redis server certificate.`

- Comment / default documentation.

**L1353** `;ha_redis_tls_server_name =`

- Comment / default documentation.

**L1354** ``

- Blank line.

**L1355** `# Skips validating the Redis server certificate.`

- Comment / default documentation.

**L1356** `;ha_redis_tls_insecure_skip_verify =`

- Comment / default documentation.

**L1357** ``

- Blank line.

**L1358** `# Overrides the default TLS cipher suite list.`

- Comment / default documentation.

**L1359** `;ha_redis_tls_cipher_suites =`

- Comment / default documentation.

**L1360** ``

- Blank line.

**L1361** `# Overrides the default minimum TLS version.`

- Comment / default documentation.

**L1362** `# Allowed values: VersionTLS10, VersionTLS11, VersionTLS12, VersionTLS13`

- Comment / default documentation.

**L1363** `;ha_redis_tls_min_version =`

- Comment / default documentation.

**L1364** ``

- Blank line.

**L1365** `# Listen address/hostname and port to receive unified alerting messages for other Grafana instances. The port is used for both TCP and UDP. It is assumed other Grafana instances are also running on the same port. The default value is \`0.0.0.0:9094\`.`

- Comment / default documentation.

**L1366** `;ha_listen_address = "0.0.0.0:9094"`

- Comment / default documentation.

**L1367** ``

- Blank line.

**L1368** `# Listen address/hostname and port to receive unified alerting messages for other Grafana instances. The port is used for both TCP and UDP. It is assumed other Grafana instances are also running on the same port. The default value is \`0.0.0.0:9094\`.`

- Comment / default documentation.

**L1369** `;ha_advertise_address = ""`

- Comment / default documentation.

**L1370** ``

- Blank line.

**L1371** `# Comma-separated list of initial instances (in a format of host:port) that will form the HA cluster. Configuring this setting will enable High Availability mode for alerting.`

- Comment / default documentation.

**L1372** `;ha_peers = ""`

- Comment / default documentation.

**L1373** ``

- Blank line.

**L1374** `# Time to wait for an instance to send a notification via the Alertmanager. In HA, each Grafana instance will`

- Comment / default documentation.

**L1375** `# be assigned a position (e.g. 0, 1). We then multiply this position with the timeout to indicate how long should`

- Comment / default documentation.

**L1376** `# each instance wait before sending the notification to take into account replication lag.`

- Comment / default documentation.

**L1377** `# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1378** `;ha_peer_timeout = "15s"`

- Comment / default documentation.

**L1379** ``

- Blank line.

**L1380** `# The label is an optional string to include on each packet and stream.`

- Comment / default documentation.

**L1381** `# It uniquely identifies the cluster and prevents cross-communication`

- Comment / default documentation.

**L1382** `# issues when sending gossip messages in an enviromenet with multiple clusters.`

- Comment / default documentation.

**L1383** `;ha_label =`

- Comment / default documentation.

**L1384** ``

- Blank line.

**L1385** `# The interval between sending gossip messages. By lowering this value (more frequent) gossip messages are propagated`

- Comment / default documentation.

**L1386** `# across cluster more quickly at the expense of increased bandwidth usage.`

- Comment / default documentation.

**L1387** `# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1388** `;ha_gossip_interval = "200ms"`

- Comment / default documentation.

**L1389** ``

- Blank line.

**L1390** `# Length of time to attempt to reconnect to a lost peer. Recommended to be short (<15m) when Grafana is running in a Kubernetes cluster.`

- Comment / default documentation.

**L1391** `# The string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1392** `;ha_reconnect_timeout = 6h`

- Comment / default documentation.

**L1393** ``

- Blank line.

**L1394** `# The interval between gossip full state syncs. Setting this interval lower (more frequent) will increase convergence speeds`

- Comment / default documentation.

**L1395** `# across larger clusters at the expense of increased bandwidth usage.`

- Comment / default documentation.

**L1396** `# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1397** `;ha_push_pull_interval = "60s"`

- Comment / default documentation.

**L1398** ``

- Blank line.

**L1399** `# Enable or disable alerting rule execution. The alerting UI remains visible.`

- Comment / default documentation.

**L1400** `;execute_alerts = true`

- Comment / default documentation.

**L1401** ``

- Blank line.

**L1402** `# Alert evaluation timeout when fetching data from the datasource.`

- Comment / default documentation.

**L1403** `# The timeout string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1404** `;evaluation_timeout = 30s`

- Comment / default documentation.

**L1405** ``

- Blank line.

**L1406** `# Total number of evaluation attempts for an alert rule before giving up (including the initial attempt). The default value is 3.`

- Comment / default documentation.

**L1407** `# The retry mechanism will stop if this number is reached or if the rule's evaluation interval is exceeded.`

- Comment / default documentation.

**L1408** `# NOTE: For rules with short evaluation intervals, it's recommended to keep this value low and ensure that`

- Comment / default documentation.

**L1409** `# retry delays are shorter than the rule's evaluation interval to avoid resource contention.`

- Comment / default documentation.

**L1410** `;max_attempts = 3`

- Comment / default documentation.

**L1411** ``

- Blank line.

**L1412** `# The initial delay before retrying a failed alert evaluation. This is the starting point for exponential backoff.`

- Comment / default documentation.

**L1413** `;initial_retry_delay = 1s`

- Comment / default documentation.

**L1414** ``

- Blank line.

**L1415** `# The maximum delay between retries during exponential backoff. Once this delay is reached, all subsequent retries will use this fixed interval.`

- Comment / default documentation.

**L1416** `# For optimal performance, ensure the total time of all retries is less than the rule's evaluation interval to prevent retry attempts from overlapping with scheduled evaluations.`

- Comment / default documentation.

**L1417** `;max_retry_delay = 4s`

- Comment / default documentation.

**L1418** ``

- Blank line.

**L1419** `# The randomization factor for exponential backoff retries. This adds jitter to retry delays to prevent thundering herd problems when multiple rules fail simultaneously.`

- Comment / default documentation.

**L1420** `# Value must be between 0 and 1. With factor F, the actual delay will be randomly chosen`

- Comment / default documentation.

**L1421** `# from [current_delay*(1-F), current_delay*(1+F)] where current_delay grows exponentially.`

- Comment / default documentation.

**L1422** `# Default is 0.1.`

- Comment / default documentation.

**L1423** `;randomization_factor = 0.1`

- Comment / default documentation.

**L1424** ``

- Blank line.

**L1425** `# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1426** `;min_interval = 10s`

- Comment / default documentation.

**L1427** ``

- Blank line.

**L1428** `# This is an experimental option to add parallelization to saving alert states in the database.`

- Comment / default documentation.

**L1429** `# It configures the maximum number of concurrent queries per rule evaluated. The default value is 1`

- Comment / default documentation.

**L1430** `# (concurrent queries per rule disabled).`

- Comment / default documentation.

**L1431** `;max_state_save_concurrency = 1`

- Comment / default documentation.

**L1432** ``

- Blank line.

**L1433** `# If the feature flag 'alertingSaveStatePeriodic' is enabled, this is the interval that is used to persist the alerting instances to the database.`

- Comment / default documentation.

**L1434** `# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.`

- Comment / default documentation.

**L1435** `;state_periodic_save_interval = 5m`

- Comment / default documentation.

**L1436** ``

- Blank line.

**L1437** `# If the feature flag 'alertingSaveStatePeriodic' is enabled, this is the size of the batch that is saved to the database at once.`

- Comment / default documentation.

**L1438** `;state_periodic_save_batch_size = 1`

- Comment / default documentation.

**L1439** ``

- Blank line.

**L1440** `# Enable jitter for periodic state saves to distribute database load over time.`

- Comment / default documentation.

**L1441** `# When enabled, batches of alert instances are saved with calculated delays between them,`

- Comment / default documentation.

**L1442** `# preventing all instances from being written to the database simultaneously.`

- Comment / default documentation.

**L1443** `# This helps reduce database load spikes during periodic saves, especially beneficial`

- Comment / default documentation.

**L1444** `# in environments with many alert instances or high database contention.`

- Comment / default documentation.

**L1445** `# The jitter delays are distributed within 85% of the save interval to ensure completion before the next cycle.`

- Comment / default documentation.

**L1446** `;state_periodic_save_jitter_enabled = false`

- Comment / default documentation.

**L1447** ``

- Blank line.

**L1448** `# Disables the smoothing of alert evaluations across their evaluation window.`

- Comment / default documentation.

**L1449** `# Rules will evaluate in sync.`

- Comment / default documentation.

**L1450** `;disable_jitter = false`

- Comment / default documentation.

**L1451** ``

- Blank line.

**L1452** `# Retention period for Alertmanager notification log entries.`

- Comment / default documentation.

**L1453** `;notification_log_retention = 5d`

- Comment / default documentation.

**L1454** ``

- Blank line.

**L1455** `# Duration for which a resolved alert state transition will continue to be sent to the Alertmanager.`

- Comment / default documentation.

**L1456** `;resolved_alert_retention = 15m`

- Comment / default documentation.

**L1457** ``

- Blank line.

**L1458** `# Defines the limit of how many alert rule versions`

- Comment / default documentation.

**L1459** `# should be stored in the database for each alert rule in an organization including the current one.`

- Comment / default documentation.

**L1460** `# 0 value means no limit`

- Comment / default documentation.

**L1461** `;rule_version_record_limit= 0`

- Comment / default documentation.

**L1462** ``

- Blank line.

**L1463** `# The retention period for deleted alerting rules.`

- Comment / default documentation.

**L1464** `# Determines how long deleted rules are retained before being permanently removed.`

- Comment / default documentation.

**L1465** `# The retention duration must be specified using a time format with unit suffixes`

- Comment / default documentation.

**L1466** `# such as ms, s, m, h, d (e.g., 30d for 30 days).`

- Comment / default documentation.

**L1467** `# Default: 30d`

- Comment / default documentation.

**L1468** `# 0 value means that rules are deleted permanently immediately.`

- Comment / default documentation.

**L1469** `;deleted_rule_retention = 30d`

- Comment / default documentation.

**L1470** ``

- Blank line.

**L1471** `[unified_alerting.screenshots]`

- Section header: unified_alerting.screenshots

**L1472** `# Enable screenshots in notifications. You must have either installed the Grafana image rendering`

- Comment / default documentation.

**L1473** `# plugin, or set up Grafana to use a remote rendering service.`

- Comment / default documentation.

**L1474** `# For more information on configuration options, refer to [rendering].`

- Comment / default documentation.

**L1475** `;capture = false`

- Comment / default documentation.

**L1476** ``

- Blank line.

**L1477** `# The timeout for capturing screenshots. If a screenshot cannot be captured within the timeout then`

- Comment / default documentation.

**L1478** `# the notification is sent without a screenshot. The maximum duration is 30 seconds. This timeout`

- Comment / default documentation.

**L1479** `# should be less than the minimum Interval of all Evaluation Groups to avoid back pressure on alert`

- Comment / default documentation.

**L1480** `# rule evaluation.`

- Comment / default documentation.

**L1481** `;capture_timeout = 10s`

- Comment / default documentation.

**L1482** ``

- Blank line.

**L1483** `# The maximum number of screenshots that can be taken at the same time. This option is different from`

- Comment / default documentation.

**L1484** `# concurrent_render_request_limit as max_concurrent_screenshots sets the number of concurrent screenshots`

- Comment / default documentation.

**L1485** `# that can be taken at the same time for all firing alerts where as concurrent_render_request_limit sets`

- Comment / default documentation.

**L1486** `# the total number of concurrent screenshots across all Grafana services.`

- Comment / default documentation.

**L1487** `;max_concurrent_screenshots = 5`

- Comment / default documentation.

**L1488** ``

- Blank line.

**L1489** `# Uploads screenshots to the local Grafana server or remote storage such as Azure, S3 and GCS. Please`

- Comment / default documentation.

**L1490** `# see [external_image_storage] for further configuration options. If this option is false then`

- Comment / default documentation.

**L1491** `# screenshots will be persisted to disk for up to temp_data_lifetime.`

- Comment / default documentation.

**L1492** `;upload_external_image_storage = false`

- Comment / default documentation.

**L1493** ``

- Blank line.

**L1494** `[unified_alerting.reserved_labels]`

- Section header: unified_alerting.reserved_labels

**L1495** `# Comma-separated list of reserved labels added by the Grafana Alerting engine that should be disabled.`

- Comment / default documentation.

**L1496** `# For example: \`disabled_labels=grafana_folder\``

- Comment / default documentation.

**L1497** `disabled_labels =`

- Grafana setting (see Grafana documentation).

**L1498** ``

- Blank line.

**L1499** `[unified_alerting.state_history]`

- Section header: unified_alerting.state_history

**L1500** `# Enable the state history functionality in Unified Alerting. The previous states of alert rules will be visible in panels and in the UI.`

- Comment / default documentation.

**L1501** `; enabled = true`

- Comment / default documentation.

**L1502** ``

- Blank line.

**L1503** `# Select which pluggable state history backend to use. Either "annotations", "loki", "prometheus", or "multiple"`

- Comment / default documentation.

**L1504** `# "loki" writes state history to an external Loki instance.`

- Comment / default documentation.

**L1505** `# "prometheus" writes state history as GRAFANA_ALERTS metrics to a Prometheus-compatible data source.`

- Comment / default documentation.

**L1506** `# "multiple" allows history to be written to multiple backends at once.`

- Comment / default documentation.

**L1507** `# Defaults to "annotations".`

- Comment / default documentation.

**L1508** `; backend = "multiple"`

- Comment / default documentation.

**L1509** ``

- Blank line.

**L1510** `# For "multiple" only.`

- Comment / default documentation.

**L1511** `# Indicates the main backend used to serve state history queries.`

- Comment / default documentation.

**L1512** `# Either "annotations" or "loki"`

- Comment / default documentation.

**L1513** `; primary = "loki"`

- Comment / default documentation.

**L1514** ``

- Blank line.

**L1515** `# For "multiple" only.`

- Comment / default documentation.

**L1516** `# Comma-separated list of additional backends to write state history data to.`

- Comment / default documentation.

**L1517** `; secondaries = "annotations"`

- Comment / default documentation.

**L1518** ``

- Blank line.

**L1519** `# For "loki" only.`

- Comment / default documentation.

**L1520** `# URL of the external Loki instance.`

- Comment / default documentation.

**L1521** `# Either "loki_remote_url", or both of "loki_remote_read_url" and "loki_remote_write_url" is required for the "loki" backend.`

- Comment / default documentation.

**L1522** `; loki_remote_url = "http://loki:3100"`

- Comment / default documentation.

**L1523** ``

- Blank line.

**L1524** `# For "loki" only.`

- Comment / default documentation.

**L1525** `# URL of the external Loki's read path. To be used in configurations where Loki has separated read and write URLs.`

- Comment / default documentation.

**L1526** `# Either "loki_remote_url", or both of "loki_remote_read_url" and "loki_remote_write_url" is required for the "loki" backend.`

- Comment / default documentation.

**L1527** `; loki_remote_read_url = "http://loki-querier:3100"`

- Comment / default documentation.

**L1528** ``

- Blank line.

**L1529** `# For "loki" only.`

- Comment / default documentation.

**L1530** `# URL of the external Loki's write path. To be used in configurations where Loki has separated read and write URLs.`

- Comment / default documentation.

**L1531** `# Either "loki_remote_url", or both of "loki_remote_read_url" and "loki_remote_write_url" is required for the "loki" backend.`

- Comment / default documentation.

**L1532** `; loki_remote_write_url = "http://loki-distributor:3100"`

- Comment / default documentation.

**L1533** ``

- Blank line.

**L1534** `# For "loki" only.`

- Comment / default documentation.

**L1535** `# Optional tenant ID to attach to requests sent to Loki.`

- Comment / default documentation.

**L1536** `; loki_tenant_id = 123`

- Comment / default documentation.

**L1537** ``

- Blank line.

**L1538** `# For "loki" only.`

- Comment / default documentation.

**L1539** `# Optional username for basic authentication on requests sent to Loki. Can be left blank to disable basic auth.`

- Comment / default documentation.

**L1540** `; loki_basic_auth_username = "myuser"`

- Comment / default documentation.

**L1541** ``

- Blank line.

**L1542** `# For "loki" only.`

- Comment / default documentation.

**L1543** `# Optional password for basic authentication on requests sent to Loki. Can be left blank.`

- Comment / default documentation.

**L1544** `; loki_basic_auth_password = "mypass"`

- Comment / default documentation.

**L1545** ``

- Blank line.

**L1546** `# For "loki" only.`

- Comment / default documentation.

**L1547** `# Optional max query length for queries sent to Loki. Default is 721h which matches the default Loki value.`

- Comment / default documentation.

**L1548** `; loki_max_query_length = 360h`

- Comment / default documentation.

**L1549** ``

- Blank line.

**L1550** `# For "loki" only.`

- Comment / default documentation.

**L1551** `# Maximum size in bytes for queries sent to Loki. This limit is applied to user provided filters as well as system defined ones, e.g. applied by access control.`

- Comment / default documentation.

**L1552** `# If filter exceeds the limit, API returns error with code "alerting.state-history.loki.requestTooLong".`

- Comment / default documentation.

**L1553** `# Default is 64kb`

- Comment / default documentation.

**L1554** `;loki_max_query_size = 65536`

- Comment / default documentation.

**L1555** ``

- Blank line.

**L1556** `# For "prometheus" only.`

- Comment / default documentation.

**L1557** `# Target datasource UID for writing GRAFANA_ALERTS metrics.`

- Comment / default documentation.

**L1558** `; prometheus_target_datasource_uid = "my-prometheus-uid"`

- Comment / default documentation.

**L1559** ``

- Blank line.

**L1560** `# For "prometheus" only.`

- Comment / default documentation.

**L1561** `# Metric name for the GRAFANA_ALERTS metric. Default is "GRAFANA_ALERTS".`

- Comment / default documentation.

**L1562** `; prometheus_metric_name = "GRAFANA_ALERTS"`

- Comment / default documentation.

**L1563** ``

- Blank line.

**L1564** `# For "prometheus" only.`

- Comment / default documentation.

**L1565** `# Timeout for writing GRAFANA_ALERTS metrics to the target datasource. Default is 10s.`

- Comment / default documentation.

**L1566** `; prometheus_write_timeout = 10s`

- Comment / default documentation.

**L1567** ``

- Blank line.

**L1568** `[unified_alerting.state_history.external_labels]`

- Section header: unified_alerting.state_history.external_labels

**L1569** `# Optional extra labels to attach to outbound state history records or log streams.`

- Comment / default documentation.

**L1570** `# Any number of label key-value-pairs can be provided.`

- Comment / default documentation.

**L1571** `; mylabelkey = mylabelvalue`

- Comment / default documentation.

**L1572** ``

- Blank line.

**L1573** `[unified_alerting.state_history.annotations]`

- Section header: unified_alerting.state_history.annotations

**L1574** `# This section controls retention of annotations automatically created while evaluating alert rules`

- Comment / default documentation.

**L1575** `# when alerting state history backend is configured to be annotations (a setting [unified_alerting.state_history].backend`

- Comment / default documentation.

**L1576** ``

- Blank line.

**L1577** `# Configures for how long alert annotations are stored. Default is 0, which keeps them forever.`

- Comment / default documentation.

**L1578** `# This setting should be expressed as an duration. Ex 6h (hours), 10d (days), 2w (weeks), 1M (month).`

- Comment / default documentation.

**L1579** `max_age =`

- Grafana setting (see Grafana documentation).

**L1580** ``

- Blank line.

**L1581** `# Configures max number of alert annotations that Grafana stores. Default value is 0, which keeps all alert annotations.`

- Comment / default documentation.

**L1582** `max_annotations_to_keep =`

- Grafana setting (see Grafana documentation).

**L1583** ``

- Blank line.

**L1584** `[unified_alerting.notification_history]`

- Section header: unified_alerting.notification_history

**L1585** `# Enable the notification history functionality in Unified Alerting.`

- Comment / default documentation.

**L1586** `# Alertmanager notification logs will be stored in Loki.`

- Comment / default documentation.

**L1587** `; enabled = false`

- Comment / default documentation.

**L1588** ``

- Blank line.

**L1589** `# URL of the Loki instance.`

- Comment / default documentation.

**L1590** `; loki_remote_url =`

- Comment / default documentation.

**L1591** ``

- Blank line.

**L1592** `# Optional tenant ID to attach to requests sent to Loki.`

- Comment / default documentation.

**L1593** `; loki_tenant_id =`

- Comment / default documentation.

**L1594** ``

- Blank line.

**L1595** `# Optional username for basic authentication on requests sent to Loki. Can be left blank to disable basic auth.`

- Comment / default documentation.

**L1596** `; loki_basic_auth_username =`

- Comment / default documentation.

**L1597** ``

- Blank line.

**L1598** `# Optional password for basic authentication on requests sent to Loki. Can be left blank.`

- Comment / default documentation.

**L1599** `; loki_basic_auth_password =`

- Comment / default documentation.

**L1600** ``

- Blank line.

**L1601** `[unified_alerting.notification_history.external_labels]`

- Section header: unified_alerting.notification_history.external_labels

**L1602** `# Optional extra labels to attach to outbound notification history records or log streams.`

- Comment / default documentation.

**L1603** `# Any number of label key-value-pairs can be provided.`

- Comment / default documentation.

**L1604** `; mylabelkey = mylabelvalue`

- Comment / default documentation.

**L1605** ``

- Blank line.

**L1606** `[unified_alerting.prometheus_conversion]`

- Section header: unified_alerting.prometheus_conversion

**L1607** `# Configuration options for converting Prometheus alerting and recording rules to Grafana rules.`

- Comment / default documentation.

**L1608** `# These settings affect rules created via the Prometheus conversion API.`

- Comment / default documentation.

**L1609** ``

- Blank line.

**L1610** `# Offset the rule evaluation time for imported rules by a specified duration in the past.`

- Comment / default documentation.

**L1611** `# This offset is applied and saved to the rule query during the conversion process from Prometheus to Grafana format.`

- Comment / default documentation.

**L1612** `# The setting only affects rules imported after the configuration change is made and does not modify existing rules.`

- Comment / default documentation.

**L1613** `# Accepts duration formats like: 30s, 1m, 1h.`

- Comment / default documentation.

**L1614** `rule_query_offset = 1m`

- Grafana setting (see Grafana documentation).

**L1615** ``

- Blank line.

**L1616** `#################################### Recording Rules #####################`

- Comment / default documentation.

**L1617** `[recording_rules]`

- Section header: recording_rules

**L1618** `# Enable recording rules.`

- Comment / default documentation.

**L1619** `enabled = true`

- Grafana setting (see Grafana documentation).

**L1620** ``

- Blank line.

**L1621** `# Request timeout for recording rule writes.`

- Comment / default documentation.

**L1622** `timeout = 30s`

- Data proxy request timeout (seconds).

**L1623** ``

- Blank line.

**L1624** `# Default data source UID to write to if not specified in the rule definition.`

- Comment / default documentation.

**L1625** `default_datasource_uid =`

- Grafana setting (see Grafana documentation).

**L1626** ``

- Blank line.

**L1627** `# Optional custom headers to include in recording rule write requests.`

- Comment / default documentation.

**L1628** `[recording_rules.custom_headers]`

- Section header: recording_rules.custom_headers

**L1629** `# exampleHeader = exampleValue`

- Comment / default documentation.

**L1630** ``

- Blank line.

**L1631** `#################################### Annotations #########################`

- Comment / default documentation.

**L1632** `[annotations]`

- Section header: annotations

**L1633** `# Configures the batch size for the annotation clean-up job. This setting is used for dashboard, API, and alert annotations.`

- Comment / default documentation.

**L1634** `;cleanupjob_batchsize = 100`

- Comment / default documentation.

**L1635** ``

- Blank line.

**L1636** `# Enforces the maximum allowed length of the tags for any newly introduced annotations. It can be between 500 and 4096 inclusive (which is the respective's column length). Default value is 500.`

- Comment / default documentation.

**L1637** `# Setting it to a higher value would impact performance therefore is not recommended.`

- Comment / default documentation.

**L1638** `;tags_length = 500`

- Comment / default documentation.

**L1639** ``

- Blank line.

**L1640** `[annotations.dashboard]`

- Section header: annotations.dashboard

**L1641** `# Dashboard annotations means that annotations are associated with the dashboard they are created on.`

- Comment / default documentation.

**L1642** ``

- Blank line.

**L1643** `# Configures how long dashboard annotations are stored. Default is 0, which keeps them forever.`

- Comment / default documentation.

**L1644** `# This setting should be expressed as a duration. Examples: 6h (hours), 10d (days), 2w (weeks), 1M (month).`

- Comment / default documentation.

**L1645** `;max_age =`

- Comment / default documentation.

**L1646** ``

- Blank line.

**L1647** `# Configures max number of dashboard annotations that Grafana stores. Default value is 0, which keeps all dashboard annotations.`

- Comment / default documentation.

**L1648** `;max_annotations_to_keep =`

- Comment / default documentation.

**L1649** ``

- Blank line.

**L1650** `[annotations.api]`

- Section header: annotations.api

**L1651** `# API annotations means that the annotations have been created using the API without any`

- Comment / default documentation.

**L1652** `# association with a dashboard.`

- Comment / default documentation.

**L1653** ``

- Blank line.

**L1654** `# Configures how long Grafana stores API annotations. Default is 0, which keeps them forever.`

- Comment / default documentation.

**L1655** `# This setting should be expressed as a duration. Examples: 6h (hours), 10d (days), 2w (weeks), 1M (month).`

- Comment / default documentation.

**L1656** `;max_age =`

- Comment / default documentation.

**L1657** ``

- Blank line.

**L1658** `# Configures max number of API annotations that Grafana keeps. Default value is 0, which keeps all API annotations.`

- Comment / default documentation.

**L1659** `;max_annotations_to_keep =`

- Comment / default documentation.

**L1660** ``

- Blank line.

**L1661** `#################################### Explore #############################`

- Comment / default documentation.

**L1662** `[explore]`

- Section header: explore

**L1663** `# Enable the Explore section`

- Comment / default documentation.

**L1664** `;enabled = true`

- Comment / default documentation.

**L1665** ``

- Blank line.

**L1666** `#################################### Help #############################`

- Comment / default documentation.

**L1667** `[help]`

- Section header: help

**L1668** `# Enable the Help section`

- Comment / default documentation.

**L1669** `;enabled = true`

- Comment / default documentation.

**L1670** ``

- Blank line.

**L1671** `#################################### Profile #############################`

- Comment / default documentation.

**L1672** `[profile]`

- Section header: profile

**L1673** `# Enable the Profile section`

- Comment / default documentation.

**L1674** `;enabled = true`

- Comment / default documentation.

**L1675** ``

- Blank line.

**L1676** `#################################### News #############################`

- Comment / default documentation.

**L1677** `[news]`

- Section header: news

**L1678** `# Enable the news feed section`

- Comment / default documentation.

**L1679** `; news_feed_enabled = true`

- Comment / default documentation.

**L1680** ``

- Blank line.

**L1681** `#################################### Query #############################`

- Comment / default documentation.

**L1682** `[query]`

- Section header: query

**L1683** `# Set the number of data source queries that can be executed concurrently in mixed queries. Default is the number of CPUs.`

- Comment / default documentation.

**L1684** `concurrent_query_limit = 20`

- Limit concurrent mixed queries.

**L1685** ``

- Blank line.

**L1686** `#################################### Query History #############################`

- Comment / default documentation.

**L1687** `[query_history]`

- Section header: query_history

**L1688** `# Enable the Query history`

- Comment / default documentation.

**L1689** `;enabled = true`

- Comment / default documentation.

**L1690** ``

- Blank line.

**L1691** `#################################### Short Links #############################`

- Comment / default documentation.

**L1692** `[short_links]`

- Section header: short_links

**L1693** `# Short links which are never accessed will be deleted as cleanup. Time is in days. Default is 7 days. Max is 365. 0 means they will be deleted approximately every 10 minutes.`

- Comment / default documentation.

**L1694** `;expire_time = 7`

- Comment / default documentation.

**L1695** ``

- Blank line.

**L1696** `#################################### Internal Grafana Metrics ##########################`

- Comment / default documentation.

**L1697** `# Metrics available at HTTP URL /metrics and /metrics/plugins/:pluginId`

- Comment / default documentation.

**L1698** `[metrics]`

- Section header: metrics

**L1699** `# Disable / Enable internal metrics`

- Comment / default documentation.

**L1700** `;enabled           = true`

- Comment / default documentation.

**L1701** `# Graphite Publish interval`

- Comment / default documentation.

**L1702** `;interval_seconds  = 10`

- Comment / default documentation.

**L1703** `# Disable total stats (stat_totals_*) metrics to be generated`

- Comment / default documentation.

**L1704** `;disable_total_stats = false`

- Comment / default documentation.

**L1705** `# The interval at which the total stats collector will update the stats. Default is 1800 seconds.`

- Comment / default documentation.

**L1706** `;total_stats_collector_interval_seconds = 1800`

- Comment / default documentation.

**L1707** ``

- Blank line.

**L1708** `#If both are set, basic auth will be required for the metrics endpoints.`

- Comment / default documentation.

**L1709** `; basic_auth_username =`

- Comment / default documentation.

**L1710** `; basic_auth_password =`

- Comment / default documentation.

**L1711** ``

- Blank line.

**L1712** `# Metrics environment info adds dimensions to the \`grafana_environment_info\` metric, which`

- Comment / default documentation.

**L1713** `# can expose more information about the Grafana instance.`

- Comment / default documentation.

**L1714** `[metrics.environment_info]`

- Section header: metrics.environment_info

**L1715** `#exampleLabel1 = exampleValue1`

- Comment / default documentation.

**L1716** `#exampleLabel2 = exampleValue2`

- Comment / default documentation.

**L1717** ``

- Blank line.

**L1718** `# Send internal metrics to Graphite`

- Comment / default documentation.

**L1719** `[metrics.graphite]`

- Section header: metrics.graphite

**L1720** `# Enable by setting the address setting (ex localhost:2003)`

- Comment / default documentation.

**L1721** `;address =`

- Comment / default documentation.

**L1722** `;prefix = prod.grafana.%(instance_name)s.`

- Comment / default documentation.

**L1723** ``

- Blank line.

**L1724** `#################################### Grafana.com integration  ##########################`

- Comment / default documentation.

**L1725** `# Url used to import dashboards directly from Grafana.com`

- Comment / default documentation.

**L1726** `[grafana_com]`

- Section header: grafana_com

**L1727** `;url = https://grafana.com`

- Comment / default documentation.

**L1728** `;api_url = https://grafana.com/api`

- Comment / default documentation.

**L1729** `# Grafana instance - Grafana.com integration SSO API token`

- Comment / default documentation.

**L1730** `;sso_api_token = ""`

- Comment / default documentation.

**L1731** ``

- Blank line.

**L1732** `#################################### Distributed tracing ############`

- Comment / default documentation.

**L1733** `# Opentracing is deprecated use opentelemetry instead`

- Comment / default documentation.

**L1734** `[tracing.jaeger]`

- Section header: tracing.jaeger

**L1735** `# Enable by setting the address sending traces to jaeger (ex localhost:6831)`

- Comment / default documentation.

**L1736** `;address = localhost:6831`

- Comment / default documentation.

**L1737** `# Tag that will always be included in when creating new spans. ex (tag1:value1,tag2:value2)`

- Comment / default documentation.

**L1738** `;always_included_tag = tag1:value1`

- Comment / default documentation.

**L1739** `# Type specifies the type of the sampler: const, probabilistic, rateLimiting, or remote`

- Comment / default documentation.

**L1740** `;sampler_type = const`

- Comment / default documentation.

**L1741** `# jaeger samplerconfig param`

- Comment / default documentation.

**L1742** `# for "const" sampler, 0 or 1 for always false/true respectively`

- Comment / default documentation.

**L1743** `# for "probabilistic" sampler, a probability between 0 and 1`

- Comment / default documentation.

**L1744** `# for "rateLimiting" sampler, the number of spans per second`

- Comment / default documentation.

**L1745** `# for "remote" sampler, param is the same as for "probabilistic"`

- Comment / default documentation.

**L1746** `# and indicates the initial sampling rate before the actual one`

- Comment / default documentation.

**L1747** `# is received from the mothership`

- Comment / default documentation.

**L1748** `;sampler_param = 1`

- Comment / default documentation.

**L1749** `# sampling_server_url is the URL of a sampling manager providing a sampling strategy.`

- Comment / default documentation.

**L1750** `;sampling_server_url =`

- Comment / default documentation.

**L1751** `# Whether or not to use Zipkin propagation (x-b3- HTTP headers).`

- Comment / default documentation.

**L1752** `;zipkin_propagation = false`

- Comment / default documentation.

**L1753** `# Setting this to true disables shared RPC spans.`

- Comment / default documentation.

**L1754** `# Not disabling is the most common setting when using Zipkin elsewhere in your infrastructure.`

- Comment / default documentation.

**L1755** `;disable_shared_zipkin_spans = false`

- Comment / default documentation.

**L1756** ``

- Blank line.

**L1757** `[tracing.opentelemetry]`

- Section header: tracing.opentelemetry

**L1758** `# attributes that will always be included in when creating new spans. ex (key1:value1,key2:value2)`

- Comment / default documentation.

**L1759** `;custom_attributes = key1:value1,key2:value2`

- Comment / default documentation.

**L1760** `# Type specifies the type of the sampler: const, probabilistic, rateLimiting, or remote`

- Comment / default documentation.

**L1761** `; sampler_type = remote`

- Comment / default documentation.

**L1762** `# Sampler configuration parameter`

- Comment / default documentation.

**L1763** `# for "const" sampler, 0 or 1 for always false/true respectively`

- Comment / default documentation.

**L1764** `# for "probabilistic" sampler, a probability between 0.0 and 1.0`

- Comment / default documentation.

**L1765** `# for "rateLimiting" sampler, the number of spans per second`

- Comment / default documentation.

**L1766** `# for "remote" sampler, param is the same as for "probabilistic"`

- Comment / default documentation.

**L1767** `#   and indicates the initial sampling rate before the actual one`

- Comment / default documentation.

**L1768** `#   is received from the sampling server (set at sampling_server_url)`

- Comment / default documentation.

**L1769** `; sampler_param = 0.5`

- Comment / default documentation.

**L1770** `# specifies the URL of the sampling server when sampler_type is remote`

- Comment / default documentation.

**L1771** `; sampling_server_url = http://localhost:5778/sampling`

- Comment / default documentation.

**L1772** ``

- Blank line.

**L1773** `[tracing.opentelemetry.jaeger]`

- Section header: tracing.opentelemetry.jaeger

**L1774** `# jaeger destination (ex http://localhost:14268/api/traces)`

- Comment / default documentation.

**L1775** `; address = http://localhost:14268/api/traces`

- Comment / default documentation.

**L1776** `# Propagation specifies the text map propagation format: w3c, jaeger`

- Comment / default documentation.

**L1777** `; propagation = jaeger`

- Comment / default documentation.

**L1778** ``

- Blank line.

**L1779** `# This is a configuration for OTLP exporter with GRPC protocol`

- Comment / default documentation.

**L1780** `[tracing.opentelemetry.otlp]`

- Section header: tracing.opentelemetry.otlp

**L1781** `# otlp destination (ex localhost:4317)`

- Comment / default documentation.

**L1782** `; address = localhost:4317`

- Comment / default documentation.

**L1783** `# Propagation specifies the text map propagation format: w3c, jaeger`

- Comment / default documentation.

**L1784** `; propagation = w3c`

- Comment / default documentation.

**L1785** `# Toggles the insecure communication setting, defaults to \`true\`.`

- Comment / default documentation.

**L1786** `# When set to \`false\`, the OTLP client will use TLS credentials with the default system cert pool for communication.`

- Comment / default documentation.

**L1787** `; insecure = false`

- Comment / default documentation.

**L1788** ``

- Blank line.

**L1789** `#################################### External image storage ##########################`

- Comment / default documentation.

**L1790** `[external_image_storage]`

- Section header: external_image_storage

**L1791** `# Used for uploading images to public servers so they can be included in slack/email messages.`

- Comment / default documentation.

**L1792** `# you can choose between (s3, webdav, gcs, azure_blob, local)`

- Comment / default documentation.

**L1793** `;provider =`

- Comment / default documentation.

**L1794** ``

- Blank line.

**L1795** `[external_image_storage.s3]`

- Section header: external_image_storage.s3

**L1796** `;endpoint =`

- Comment / default documentation.

**L1797** `;path_style_access =`

- Comment / default documentation.

**L1798** `;bucket =`

- Comment / default documentation.

**L1799** `;region =`

- Comment / default documentation.

**L1800** `;path =`

- Comment / default documentation.

**L1801** `;access_key =`

- Comment / default documentation.

**L1802** `;secret_key =`

- Comment / default documentation.

**L1803** ``

- Blank line.

**L1804** `[external_image_storage.webdav]`

- Section header: external_image_storage.webdav

**L1805** `;url =`

- Comment / default documentation.

**L1806** `;username =`

- Comment / default documentation.

**L1807** `;password =`

- Comment / default documentation.

**L1808** `;public_url =`

- Comment / default documentation.

**L1809** ``

- Blank line.

**L1810** `[external_image_storage.gcs]`

- Section header: external_image_storage.gcs

**L1811** `;key_file =`

- Comment / default documentation.

**L1812** `;bucket =`

- Comment / default documentation.

**L1813** `;path =`

- Comment / default documentation.

**L1814** `;enable_signed_urls = false`

- Comment / default documentation.

**L1815** `;signed_url_expiration =`

- Comment / default documentation.

**L1816** ``

- Blank line.

**L1817** `[external_image_storage.azure_blob]`

- Section header: external_image_storage.azure_blob

**L1818** `;account_name =`

- Comment / default documentation.

**L1819** `;account_key =`

- Comment / default documentation.

**L1820** `;container_name =`

- Comment / default documentation.

**L1821** `;sas_token_expiration_days =`

- Comment / default documentation.

**L1822** ``

- Blank line.

**L1823** `[external_image_storage.local]`

- Section header: external_image_storage.local

**L1824** `# does not require any configuration`

- Comment / default documentation.

**L1825** ``

- Blank line.

**L1826** `[rendering]`

- Section header: rendering

**L1827** `# Options to configure a remote HTTP image rendering service, e.g. using https://github.com/grafana/grafana-image-renderer.`

- Comment / default documentation.

**L1828** `# URL to a remote HTTP image renderer service, e.g. http://localhost:8081/render, will enable Grafana to render panels and dashboards to PNG-images using HTTP requests to an external service.`

- Comment / default documentation.

**L1829** `;server_url =`

- Comment / default documentation.

**L1830** `# If the remote HTTP image renderer service runs on a different server than the Grafana server you may have to configure this to a URL where Grafana is reachable, e.g. http://grafana.domain/.`

- Comment / default documentation.

**L1831** `;callback_url =`

- Comment / default documentation.

**L1832** `# An auth token that will be sent to and verified by the renderer. The renderer will deny any request without an auth token matching the one configured on the renderer side.`

- Comment / default documentation.

**L1833** `;renderer_token = -`

- Comment / default documentation.

**L1834** `# Concurrent render request limit affects when the /render HTTP endpoint is used. Rendering many images at the same time can overload the server,`

- Comment / default documentation.

**L1835** `# which this setting can help protect against by only allowing a certain amount of concurrent requests.`

- Comment / default documentation.

**L1836** `;concurrent_render_request_limit = 30`

- Comment / default documentation.

**L1837** `# Determines the lifetime of the render key used by the image renderer to access and render Grafana.`

- Comment / default documentation.

**L1838** `# This setting should be expressed as a duration. Examples: 10s (seconds), 5m (minutes), 2h (hours).`

- Comment / default documentation.

**L1839** `# Default is 5m. This should be more than enough for most deployments.`

- Comment / default documentation.

**L1840** `# Change the value only if image rendering is failing and you see \`Failed to get the render key from cache\` in Grafana logs.`

- Comment / default documentation.

**L1841** `;render_key_lifetime = 5m`

- Comment / default documentation.

**L1842** `# Default width for panel screenshot`

- Comment / default documentation.

**L1843** `;default_image_width = 1000`

- Comment / default documentation.

**L1844** `# Default height for panel screenshot`

- Comment / default documentation.

**L1845** `;default_image_height = 500`

- Comment / default documentation.

**L1846** `# Default scale for panel screenshot`

- Comment / default documentation.

**L1847** `;default_image_scale = 1`

- Comment / default documentation.

**L1848** ``

- Blank line.

**L1849** `[panels]`

- Section header: panels

**L1850** `# If set to true Grafana will allow script tags in text panels. Not recommended as it enable XSS vulnerabilities.`

- Comment / default documentation.

**L1851** `;disable_sanitize_html = false`

- Comment / default documentation.

**L1852** ``

- Blank line.

**L1853** `[plugins]`

- Section header: plugins

**L1854** `;enable_alpha = false`

- Comment / default documentation.

**L1855** `;app_tls_skip_verify_insecure = false`

- Comment / default documentation.

**L1856** `# Enter a comma-separated list of plugin identifiers to identify plugins to load even if they are unsigned. Plugins with modified signatures are never loaded.`

- Comment / default documentation.

**L1857** `;allow_loading_unsigned_plugins =`

- Comment / default documentation.

**L1858** `# Enable or disable installing / uninstalling / updating plugins directly from within Grafana.`

- Comment / default documentation.

**L1859** `;plugin_admin_enabled = false`

- Comment / default documentation.

**L1860** `;plugin_admin_external_manage_enabled = false`

- Comment / default documentation.

**L1861** `;plugin_catalog_url = https://grafana.com/grafana/plugins/`

- Comment / default documentation.

**L1862** `# Enter a comma-separated list of plugin identifiers to hide in the plugin catalog.`

- Comment / default documentation.

**L1863** `;plugin_catalog_hidden_plugins =`

- Comment / default documentation.

**L1864** `# Log all backend requests for core and external plugins.`

- Comment / default documentation.

**L1865** `;log_backend_requests = false`

- Comment / default documentation.

**L1866** `# Disable download of the public key for verifying plugin signature.`

- Comment / default documentation.

**L1867** `; public_key_retrieval_disabled = false`

- Comment / default documentation.

**L1868** `# Force download of the public key for verifying plugin signature on startup. If disabled, the public key will be retrieved every 10 days.`

- Comment / default documentation.

**L1869** `# Requires public_key_retrieval_disabled to be false to have any effect.`

- Comment / default documentation.

**L1870** `; public_key_retrieval_on_startup = false`

- Comment / default documentation.

**L1871** `# Enter a comma-separated list of plugin identifiers to avoid loading (including core plugins). These plugins will be hidden in the catalog.`

- Comment / default documentation.

**L1872** `; disable_plugins =`

- Comment / default documentation.

**L1873** `# Comma separated list of plugin ids to install as part of the startup process.`

- Comment / default documentation.

**L1874** `# These will be installed, by default, asynchronously (in the background) while starting Grafana.`

- Comment / default documentation.

**L1875** `; preinstall =`

- Comment / default documentation.

**L1876** `# Comma separated list of plugin ids to install before the startup process`

- Comment / default documentation.

**L1877** `# These will be installed before starting Grafana. Useful when used with provisioning.`

- Comment / default documentation.

**L1878** `; preinstall_sync =`

- Comment / default documentation.

**L1879** `# Disables preinstall feature. It has the same effect as setting preinstall to an empty list.`

- Comment / default documentation.

**L1880** `; preinstall_disabled = false`

- Comment / default documentation.

**L1881** ``

- Blank line.

**L1882** `#################################### Grafana Live ##########################################`

- Comment / default documentation.

**L1883** `[live]`

- Section header: live

**L1884** `# max_connections to Grafana Live WebSocket endpoint per Grafana server instance. See Grafana Live docs`

- Comment / default documentation.

**L1885** `# if you are planning to make it higher than default 100 since this can require some OS and infrastructure`

- Comment / default documentation.

**L1886** `# tuning. 0 disables Live, -1 means unlimited connections.`

- Comment / default documentation.

**L1887** `;max_connections = 100`

- Comment / default documentation.

**L1888** ``

- Blank line.

**L1889** `# allowed_origins is a comma-separated list of origins that can establish connection with Grafana Live.`

- Comment / default documentation.

**L1890** `# If not set then origin will be matched over root_url. Supports wildcard symbol "*".`

- Comment / default documentation.

**L1891** `;allowed_origins =`

- Comment / default documentation.

**L1892** ``

- Blank line.

**L1893** `# engine defines an HA (high availability) engine to use for Grafana Live. By default no engine used - in`

- Comment / default documentation.

**L1894** `# this case Live features work only on a single Grafana server. Available options: "redis".`

- Comment / default documentation.

**L1895** `;ha_engine =`

- Comment / default documentation.

**L1896** ``

- Blank line.

**L1897** `# ha_engine_address sets a connection address for Live HA engine. Depending on engine type address format can differ.`

- Comment / default documentation.

**L1898** `# For now we only support Redis connection address in "host:port" format.`

- Comment / default documentation.

**L1899** `;ha_engine_address = "127.0.0.1:6379"`

- Comment / default documentation.

**L1900** ``

- Blank line.

**L1901** `# ha_engine_password allows setting an optional password to authenticate with the engine`

- Comment / default documentation.

**L1902** `;ha_engine_password = ""`

- Comment / default documentation.

**L1903** ``

- Blank line.

**L1904** `# ha_prefix is a prefix for keys in the HA engine. It's used to separate keys for different Grafana instances.`

- Comment / default documentation.

**L1905** `;ha_prefix =`

- Comment / default documentation.

**L1906** ``

- Blank line.

**L1907** `#################################### Grafana Image Renderer Plugin ##########################`

- Comment / default documentation.

**L1908** `[plugin.grafana-image-renderer]`

- Section header: plugin.grafana-image-renderer

**L1909** `# Instruct headless browser instance to use a default timezone when not provided by Grafana, e.g. when rendering panel image of alert.`

- Comment / default documentation.

**L1910** `# See ICU’s metaZones.txt (https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt) for a list of supported`

- Comment / default documentation.

**L1911** `# timezone IDs. Fallbacks to TZ environment variable if not set.`

- Comment / default documentation.

**L1912** `;rendering_timezone =`

- Comment / default documentation.

**L1913** ``

- Blank line.

**L1914** `# Instruct headless browser instance to use a default language when not provided by Grafana, e.g. when rendering panel image of alert.`

- Comment / default documentation.

**L1915** `# Please refer to the HTTP header Accept-Language to understand how to format this value, e.g. 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'.`

- Comment / default documentation.

**L1916** `;rendering_language =`

- Comment / default documentation.

**L1917** ``

- Blank line.

**L1918** `# Instruct headless browser instance to use a default device scale factor when not provided by Grafana, e.g. when rendering panel image of alert.`

- Comment / default documentation.

**L1919** `# Default is 1. Using a higher value will produce more detailed images (higher DPI), but will require more disk space to store an image.`

- Comment / default documentation.

**L1920** `;rendering_viewport_device_scale_factor =`

- Comment / default documentation.

**L1921** ``

- Blank line.

**L1922** `# Instruct headless browser instance whether to ignore HTTPS errors during navigation. Per default HTTPS errors are not ignored. Due to`

- Comment / default documentation.

**L1923** `# the security risk it's not recommended to ignore HTTPS errors.`

- Comment / default documentation.

**L1924** `;rendering_ignore_https_errors =`

- Comment / default documentation.

**L1925** ``

- Blank line.

**L1926** `# Instruct headless browser instance whether to capture and log verbose information when rendering an image. Default is false and will`

- Comment / default documentation.

**L1927** `# only capture and log error messages. When enabled, debug messages are captured and logged as well.`

- Comment / default documentation.

**L1928** `# For the verbose information to be included in the Grafana server log you have to adjust the rendering log level to debug, configure`

- Comment / default documentation.

**L1929** `# [log].filter = rendering:debug.`

- Comment / default documentation.

**L1930** `;rendering_verbose_logging =`

- Comment / default documentation.

**L1931** ``

- Blank line.

**L1932** `# Instruct headless browser instance whether to output its debug and error messages into running process of remote rendering service.`

- Comment / default documentation.

**L1933** `# Default is false. This can be useful to enable (true) when troubleshooting.`

- Comment / default documentation.

**L1934** `;rendering_dumpio =`

- Comment / default documentation.

**L1935** ``

- Blank line.

**L1936** `# Instruct headless browser instance whether to register metrics for the duration of every rendering step. Default is false.`

- Comment / default documentation.

**L1937** `# This can be useful to enable (true) when optimizing the rendering mode settings to improve the plugin performance or when troubleshooting.`

- Comment / default documentation.

**L1938** `;rendering_timing_metrics =`

- Comment / default documentation.

**L1939** ``

- Blank line.

**L1940** `# This is a configuration for OTLP exporter with HTTP protocol, set this URL to enable tracing (ex: http://localhost:4318/v1/traces). Default to empty (tracing disabled).`

- Comment / default documentation.

**L1941** `;rendering_tracing_url =`

- Comment / default documentation.

**L1942** ``

- Blank line.

**L1943** `# Additional arguments to pass to the headless browser instance. Default is --no-sandbox. The list of Chromium flags can be found`

- Comment / default documentation.

**L1944** `# here (https://peter.sh/experiments/chromium-command-line-switches/). Multiple arguments is separated with comma-character.`

- Comment / default documentation.

**L1945** `;rendering_args =`

- Comment / default documentation.

**L1946** ``

- Blank line.

**L1947** `# You can configure the plugin to use a different browser binary instead of the pre-packaged version of Chromium.`

- Comment / default documentation.

**L1948** `# Please note that this is not recommended, since you may encounter problems if the installed version of Chrome/Chromium is not`

- Comment / default documentation.

**L1949** `# compatible with the plugin.`

- Comment / default documentation.

**L1950** `;rendering_chrome_bin =`

- Comment / default documentation.

**L1951** ``

- Blank line.

**L1952** `# Instruct how headless browser instances are created. Default is 'default' and will create a new browser instance on each request.`

- Comment / default documentation.

**L1953** `# Mode 'clustered' will make sure that only a maximum of browsers/incognito pages can execute concurrently.`

- Comment / default documentation.

**L1954** `# Mode 'reusable' will have one browser instance and will create a new incognito page on each request.`

- Comment / default documentation.

**L1955** `;rendering_mode =`

- Comment / default documentation.

**L1956** ``

- Blank line.

**L1957** `# When rendering_mode = clustered, you can instruct how many browsers or incognito pages can execute concurrently. Default is 'browser'`

- Comment / default documentation.

**L1958** `# and will cluster using browser instances.`

- Comment / default documentation.

**L1959** `# Mode 'context' will cluster using incognito pages.`

- Comment / default documentation.

**L1960** `;rendering_clustering_mode =`

- Comment / default documentation.

**L1961** `# When rendering_mode = clustered, you can define the maximum number of browser instances/incognito pages that can execute concurrently. Default is '5'.`

- Comment / default documentation.

**L1962** `;rendering_clustering_max_concurrency =`

- Comment / default documentation.

**L1963** `# When rendering_mode = clustered, you can specify the duration a rendering request can take before it will time out. Default is \`30\` seconds.`

- Comment / default documentation.

**L1964** `;rendering_clustering_timeout =`

- Comment / default documentation.

**L1965** ``

- Blank line.

**L1966** `# Limit the maximum viewport width, height and device scale factor that can be requested.`

- Comment / default documentation.

**L1967** `;rendering_viewport_max_width =`

- Comment / default documentation.

**L1968** `;rendering_viewport_max_height =`

- Comment / default documentation.

**L1969** `;rendering_viewport_max_device_scale_factor =`

- Comment / default documentation.

**L1970** ``

- Blank line.

**L1971** `# Change the listening host and port of the gRPC server. Default host is 127.0.0.1 and default port is 0 and will automatically assign`

- Comment / default documentation.

**L1972** `# a port not in use.`

- Comment / default documentation.

**L1973** `;grpc_host =`

- Comment / default documentation.

**L1974** `;grpc_port =`

- Comment / default documentation.

**L1975** ``

- Blank line.

**L1976** `[enterprise]`

- Section header: enterprise

**L1977** `# Path to a valid Grafana Enterprise license.jwt file`

- Comment / default documentation.

**L1978** `;license_path =`

- Comment / default documentation.

**L1979** ``

- Blank line.

**L1980** `[feature_toggles]`

- Section header: feature_toggles

**L1981** `# there are currently two ways to enable feature toggles in the \`grafana.ini\`.`

- Comment / default documentation.

**L1982** `# you can either pass an array of feature you want to enable to the \`enable\` field or`

- Comment / default documentation.

**L1983** `# configure each toggle by setting the name of the toggle to true/false. Toggles set to true/false`

- Comment / default documentation.

**L1984** `# will take presidence over toggles in the \`enable\` list.`

- Comment / default documentation.

**L1985** ``

- Blank line.

**L1986** `;enable = feature1,feature2`

- Comment / default documentation.

**L1987** ``

- Blank line.

**L1988** `;feature1 = true`

- Comment / default documentation.

**L1989** `;feature2 = false`

- Comment / default documentation.

**L1990** ``

- Blank line.

**L1991** `[date_formats]`

- Section header: date_formats

**L1992** `# For information on what formatting patterns that are supported https://momentjs.com/docs/#/displaying/`

- Comment / default documentation.

**L1993** ``

- Blank line.

**L1994** `# Default system date format used in time range picker and other places where full time is displayed`

- Comment / default documentation.

**L1995** `;full_date = YYYY-MM-DD HH:mm:ss`

- Comment / default documentation.

**L1996** ``

- Blank line.

**L1997** `# Used by graph and other places where we only show small intervals`

- Comment / default documentation.

**L1998** `;interval_second = HH:mm:ss`

- Comment / default documentation.

**L1999** `;interval_minute = HH:mm`

- Comment / default documentation.

**L2000** `;interval_hour = MM/DD HH:mm`

- Comment / default documentation.

**L2001** `;interval_day = MM/DD`

- Comment / default documentation.

**L2002** `;interval_month = YYYY-MM`

- Comment / default documentation.

**L2003** `;interval_year = YYYY`

- Comment / default documentation.

**L2004** ``

- Blank line.

**L2005** `# Experimental feature`

- Comment / default documentation.

**L2006** `;use_browser_locale = false`

- Comment / default documentation.

**L2007** ``

- Blank line.

**L2008** `# Default timezone for user preferences. Options are 'browser' for the browser local timezone or a timezone name from IANA Time Zone database, e.g. 'UTC' or 'Europe/Amsterdam' etc.`

- Comment / default documentation.

**L2009** `;default_timezone = browser`

- Comment / default documentation.

**L2010** ``

- Blank line.

**L2011** `[time_picker]`

- Section header: time_picker

**L2012** `# Custom quick ranges for the time picker. Each quick range has a display name, a from value, and a to value.`

- Comment / default documentation.

**L2013** `# Format: [{"from":"now-5m","to":"now","display":"Last 5 minutes"},{"from":"now-15m","to":"now","display":"Last 15 minutes"}]`

- Comment / default documentation.

**L2014** `;quick_ranges =`

- Comment / default documentation.

**L2015** ``

- Blank line.

**L2016** `[expressions]`

- Section header: expressions

**L2017** `# Enable or disable the expressions functionality.`

- Comment / default documentation.

**L2018** `;enabled = true`

- Comment / default documentation.

**L2019** ``

- Blank line.

**L2020** `[geomap]`

- Section header: geomap

**L2021** `# Set the JSON configuration for the default basemap`

- Comment / default documentation.

**L2022** `;default_baselayer_config = \`{`

- Comment / default documentation.

**L2023** `;  "type": "xyz",`

- Comment / default documentation.

**L2024** `;  "config": {`

- Comment / default documentation.

**L2025** `;    "attribution": "Open street map",`

- Comment / default documentation.

**L2026** `;    "url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png"`

- Comment / default documentation.

**L2027** `;  }`

- Comment / default documentation.

**L2028** `;}\``

- Comment / default documentation.

**L2029** ``

- Blank line.

**L2030** `# Enable or disable loading other base map layers`

- Comment / default documentation.

**L2031** `;enable_custom_baselayers = true`

- Comment / default documentation.

**L2032** ``

- Blank line.

**L2033** `#################################### Support Bundles #####################################`

- Comment / default documentation.

**L2034** `[support_bundles]`

- Section header: support_bundles

**L2035** `# Enable support bundle creation (default: true)`

- Comment / default documentation.

**L2036** `#enabled = true`

- Comment / default documentation.

**L2037** `# Only server admins can generate and view support bundles (default: true)`

- Comment / default documentation.

**L2038** `#server_admin_only = true`

- Comment / default documentation.

**L2039** `# If set, bundles will be encrypted with the provided public keys separated by whitespace`

- Comment / default documentation.

**L2040** `#public_keys = ""`

- Comment / default documentation.

**L2041** ``

- Blank line.

**L2042** `# Move an app plugin referenced by its id (including all its pages) to a specific navigation section`

- Comment / default documentation.

**L2043** `[navigation.app_sections]`

- Section header: navigation.app_sections

**L2044** `# The following will move an app plugin with the id of \`my-app-id\` under the \`cfg\` section`

- Comment / default documentation.

**L2045** `# my-app-id = cfg`

- Comment / default documentation.

**L2046** ``

- Blank line.

**L2047** `# Move a specific app plugin page (referenced by its \`path\` field) to a specific navigation section`

- Comment / default documentation.

**L2048** `[navigation.app_standalone_pages]`

- Section header: navigation.app_standalone_pages

**L2049** `# The following will move the page with the path "/a/my-app-id/my-page" from \`my-app-id\` to the \`cfg\` section`

- Comment / default documentation.

**L2050** `# /a/my-app-id/my-page = cfg`

- Comment / default documentation.

**L2051** ``

- Blank line.

**L2052** `#################################### Secure Socks5 Datasource Proxy #####################################`

- Comment / default documentation.

**L2053** `[secure_socks_datasource_proxy]`

- Section header: secure_socks_datasource_proxy

**L2054** `; enabled = false`

- Comment / default documentation.

**L2055** `; root_ca_cert =`

- Comment / default documentation.

**L2056** `; client_key =`

- Comment / default documentation.

**L2057** `; client_cert =`

- Comment / default documentation.

**L2058** `; server_name =`

- Comment / default documentation.

**L2059** `# The address of the socks5 proxy datasources should connect to`

- Comment / default documentation.

**L2060** `; proxy_address =`

- Comment / default documentation.

**L2061** `; show_ui = true`

- Comment / default documentation.

**L2062** `; allow_insecure = false`

- Comment / default documentation.

**L2063** ``

- Blank line.

**L2064** `#################################### Public Dashboards #####################################`

- Comment / default documentation.

**L2065** `[public_dashboards]`

- Section header: public_dashboards

**L2066** `# Set to false to disable public dashboards`

- Comment / default documentation.

**L2067** `;enabled = true`

- Comment / default documentation.

**L2068** ``

- Blank line.

**L2069** `###################################### Cloud Migration ######################################`

- Comment / default documentation.

**L2070** `[cloud_migration]`

- Section header: cloud_migration

**L2071** `# Set to true to enable target-side migration UI`

- Comment / default documentation.

**L2072** `;is_target = false`

- Comment / default documentation.

**L2073** `# Token used to send requests to grafana com`

- Comment / default documentation.

**L2074** `;gcom_api_token = ""`

- Comment / default documentation.

**L2075** `# How long to wait for a request sent to gms to start a snapshot to complete`

- Comment / default documentation.

**L2076** `;start_snapshot_timeout = 5s`

- Comment / default documentation.

**L2077** `# How long to wait for a request sent to gms to validate a key to complete`

- Comment / default documentation.

**L2078** `;validate_key_timeout = 5s`

- Comment / default documentation.

**L2079** `# How long to wait for a request sent to gms to get a snapshot status to complete`

- Comment / default documentation.

**L2080** `;get_snapshot_status_timeout = 5s`

- Comment / default documentation.

**L2081** `# How long to wait for a request sent to gms to create a presigned upload url`

- Comment / default documentation.

**L2082** `;create_upload_url_timeout = 5s`

- Comment / default documentation.

**L2083** `# How long to wait for a request sent to gms to report an event`

- Comment / default documentation.

**L2084** `;report_event_timeout = 5s`

- Comment / default documentation.

**L2085** `# How long to wait for a request to fetch an instance to complete`

- Comment / default documentation.

**L2086** `;fetch_instance_timeout = 5s`

- Comment / default documentation.

**L2087** `# How long to wait for a request to create an access policy to complete`

- Comment / default documentation.

**L2088** `;create_access_policy_timeout = 5s`

- Comment / default documentation.

**L2089** `# How long to wait for a request to create to fetch an access policy to complete`

- Comment / default documentation.

**L2090** `;fetch_access_policy_timeout = 5s`

- Comment / default documentation.

**L2091** `# How long to wait for a request to create to delete an access policy to complete`

- Comment / default documentation.

**L2092** `;delete_access_policy_timeout = 5s`

- Comment / default documentation.

**L2093** `# The domain name used to access cms`

- Comment / default documentation.

**L2094** `;domain = grafana-dev.net`

- Comment / default documentation.

**L2095** `# Folder used to store snapshot files. Defaults to the home dir`

- Comment / default documentation.

**L2096** `;snapshot_folder = ""`

- Comment / default documentation.

**L2097** `# How frequently should the frontend UI poll for changes while resources are migrating`

- Comment / default documentation.

**L2098** `;frontend_poll_interval = 2s`

- Comment / default documentation.

**L2099** `# Controls how the Alert Rules are migrated. Available choices: "paused" and "unchanged". Default: "paused".`

- Comment / default documentation.

**L2100** `# With "paused", all Alert Rules will be created in Paused state. This is helpful to avoid double notifications.`

- Comment / default documentation.

**L2101** `# With "unchanged", all Alert Rules will be created with the pause state unchanged coming from the source instance.`

- Comment / default documentation.

**L2102** `;alert_rules_state = "paused"`

- Comment / default documentation.

**L2103** `# Either "db" to store snapshots in the database or "fs" to store in the file system.`

- Comment / default documentation.

**L2104** `;resource_storage_type = "db"`

- Comment / default documentation.

**L2105** ``

- Blank line.

**L2106** `###################################### Secrets Manager ######################################`

- Comment / default documentation.

**L2107** `[secrets_manager]`

- Section header: secrets_manager

**L2108** `# Current key provider used for envelope encryption`

- Comment / default documentation.

**L2109** `;encryption_provider = secret_key.v1`

- Comment / default documentation.

**L2110** ``

- Blank line.

**L2111** `# These flags are required in on-prem installations for GitSync to work`

- Comment / default documentation.

**L2112** `#`

- Comment / default documentation.

**L2113** `# Whether to register the MT CRUD API`

- Comment / default documentation.

**L2114** `;register_api_server = true`

- Comment / default documentation.

**L2115** `# Whether to create the MT secrets management database`

- Comment / default documentation.

**L2116** `;run_secrets_db_migrations = true`

- Comment / default documentation.

**L2117** `# Whether to run the data key id migration. Requires that RunSecretsDBMigrations is also true.`

- Comment / default documentation.

**L2118** `;run_data_key_migration = true`

- Comment / default documentation.

**L2119** ``

- Blank line.

**L2120** `[secrets_manager.encryption.secret_key.v1]`

- Section header: secrets_manager.encryption.secret_key.v1

**L2121** `# Used to encrypt data keys`

- Comment / default documentation.

**L2122** `;secret_key = SW2YcwTIb9zpOOhoPsMm`

- Comment / default documentation.

**L2123** ``

- Blank line.

**L2124** ``

- Blank line.

**L2125** `################################## Frontend development configuration ###################################`

- Comment / default documentation.

**L2126** `# Warning! Any settings placed in this section will be available on \`process.env.frontend_dev_{foo}\` within frontend code`

- Comment / default documentation.

**L2127** `# Any values placed here may be accessible to the UI. Do not place sensitive information here.`

- Comment / default documentation.

**L2128** `[frontend_dev]`

- Section header: frontend_dev

**L2129** `# Should UI tests fail when console log/warn/erroring?`

- Comment / default documentation.

**L2130** `# Does not affect the result when running on CI - only for allowing devs to choose this behaviour locally`

- Comment / default documentation.

**L2131** `; fail_tests_on_console = true`

- Comment / default documentation.

