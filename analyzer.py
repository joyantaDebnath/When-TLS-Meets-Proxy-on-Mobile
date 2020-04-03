cipher_suites = {
'000000': {'name': 'TLS_NULL_WITH_NULL_NULL', 'protocol': 'TLS', 'kx': 'NULL', 'au': 'NULL', 'enc': 'NULL', 'bits': '0', 'mac': 'NULL', 'kxau_strength': 'NULL', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'000001': {'name': 'TLS_RSA_WITH_NULL_MD5', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'NULL', 'bits': '0', 'mac': 'MD5', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'000002': {'name': 'TLS_RSA_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'000003': {'name': 'TLS_RSA_EXPORT_WITH_RC4_40_MD5', 'protocol': 'TLS', 'kx': 'RSA_EXPORT', 'au': 'RSA_EXPORT', 'enc': 'RC4_40', 'bits': '40', 'mac': 'MD5', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000004': {'name': 'TLS_RSA_WITH_RC4_128_MD5', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'RC4_128', 'bits': '128', 'mac': 'MD5', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'000005': {'name': 'TLS_RSA_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'000006': {'name': 'TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5', 'protocol': 'TLS', 'kx': 'RSA_EXPORT', 'au': 'RSA_EXPORT', 'enc': 'RC2_CBC_40', 'bits': '40', 'mac': 'MD5', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000007': {'name': 'TLS_RSA_WITH_IDEA_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'IDEA_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000008': {'name': 'TLS_RSA_EXPORT_WITH_DES40_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA_EXPORT', 'au': 'RSA_EXPORT', 'enc': 'DES40_CBC', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000009': {'name': 'TLS_RSA_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'00000A': {'name': 'TLS_RSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00000B': {'name': 'TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'DES40_CBC', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'00000C': {'name': 'TLS_DH_DSS_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'00000D': {'name': 'TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00000E': {'name': 'TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'DES40_CBC', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'00000F': {'name': 'TLS_DH_RSA_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'000010': {'name': 'TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000011': {'name': 'TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'DES40_CBC', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000012': {'name': 'TLS_DHE_DSS_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'000013': {'name': 'TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000014': {'name': 'TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'DES40_CBC', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000015': {'name': 'TLS_DHE_RSA_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'000016': {'name': 'TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000017': {'name': 'TLS_DH_Anon_EXPORT_WITH_RC4_40_MD5', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'RC4_40', 'bits': '40', 'mac': 'MD5', 'kxau_strength': 'MiM', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000018': {'name': 'TLS_DH_Anon_WITH_RC4_128_MD5', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'RC4_128', 'bits': '128', 'mac': 'MD5', 'kxau_strength': 'MiM', 'enc_strength': 'MEDIUM', 'overall_strength': 'MiM'},
'000019': {'name': 'TLS_DH_Anon_EXPORT_WITH_DES40_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'DES40_CBC', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'00001A': {'name': 'TLS_DH_Anon_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'LOW', 'overall_strength': 'MiM'},
'00001B': {'name': 'TLS_DH_Anon_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00001C': {'name': 'SSL_FORTEZZA_KEA_WITH_NULL_SHA', 'protocol': 'SSL', 'kx': 'FORTEZZA', 'au': 'KEA', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00001D': {'name': 'SSL_FORTEZZA_KEA_WITH_FORTEZZA_CBC_SHA', 'protocol': 'SSL', 'kx': 'FORTEZZA', 'au': 'KEA', 'enc': 'FORTEZZA_CBC', 'bits': '80', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00001E': {'name': 'TLS_KRB5_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'KRB5', 'au': 'KRB5', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'00001F': {'name': 'TLS_KRB5_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'KRB5', 'au': 'KRB5', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000020': {'name': 'TLS_KRB5_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'KRB5', 'au': 'KRB5', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'000021': {'name': 'TLS_KRB5_WITH_IDEA_CBC_SHA', 'protocol': 'TLS', 'kx': 'KRB5', 'au': 'KRB5', 'enc': 'IDEA_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000022': {'name': 'TLS_KRB5_WITH_DES_CBC_MD5', 'protocol': 'TLS', 'kx': 'KRB5', 'au': 'KRB5', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'MD5', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'000023': {'name': 'TLS_KRB5_WITH_3DES_EDE_CBC_MD5', 'protocol': 'TLS', 'kx': 'KRB5', 'au': 'KRB5', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'MD5', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000024': {'name': 'TLS_KRB5_WITH_RC4_128_MD5', 'protocol': 'TLS', 'kx': 'KRB5', 'au': 'KRB5', 'enc': 'RC4_128', 'bits': '128', 'mac': 'MD5', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'000025': {'name': 'TLS_KRB5_WITH_IDEA_CBC_MD5', 'protocol': 'TLS', 'kx': 'KRB5', 'au': 'KRB5', 'enc': 'IDEA_CBC', 'bits': '128', 'mac': 'MD5', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000026': {'name': 'TLS_KRB5_EXPORT_WITH_DES_CBC_40_SHA', 'protocol': 'TLS', 'kx': 'KRB5_EXPORT', 'au': 'KRB5_EXPORT', 'enc': 'DES_CBC_40', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000027': {'name': 'TLS_KRB5_EXPORT_WITH_RC2_CBC_40_SHA', 'protocol': 'TLS', 'kx': 'KRB5_EXPORT', 'au': 'KRB5_EXPORT', 'enc': 'RC2_CBC_40', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000028': {'name': 'TLS_KRB5_EXPORT_WITH_RC4_40_SHA', 'protocol': 'TLS', 'kx': 'KRB5_EXPORT', 'au': 'KRB5_EXPORT', 'enc': 'RC4_40', 'bits': '40', 'mac': 'SHA', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000029': {'name': 'TLS_KRB5_EXPORT_WITH_DES_CBC_40_MD5', 'protocol': 'TLS', 'kx': 'KRB5_EXPORT', 'au': 'KRB5_EXPORT', 'enc': 'DES_CBC_40', 'bits': '40', 'mac': 'MD5', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'00002A': {'name': 'TLS_KRB5_EXPORT_WITH_RC2_CBC_40_MD5', 'protocol': 'TLS', 'kx': 'KRB5_EXPORT', 'au': 'KRB5_EXPORT', 'enc': 'RC2_CBC_40', 'bits': '40', 'mac': 'MD5', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'00002B': {'name': 'TLS_KRB5_EXPORT_WITH_RC4_40_MD5', 'protocol': 'TLS', 'kx': 'KRB5_EXPORT', 'au': 'KRB5_EXPORT', 'enc': 'RC4_40', 'bits': '40', 'mac': 'MD5', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'00002C': {'name': 'TLS_PSK_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00002D': {'name': 'TLS_DHE_PSK_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00002E': {'name': 'TLS_RSA_PSK_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00002F': {'name': 'TLS_RSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000030': {'name': 'TLS_DH_DSS_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000031': {'name': 'TLS_DH_RSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000032': {'name': 'TLS_DHE_DSS_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000033': {'name': 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000034': {'name': 'TLS_DH_Anon_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'000035': {'name': 'TLS_RSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000036': {'name': 'TLS_DH_DSS_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000037': {'name': 'TLS_DH_RSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000038': {'name': 'TLS_DHE_DSS_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000039': {'name': 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00003A': {'name': 'TLS_DH_Anon_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00003B': {'name': 'TLS_RSA_WITH_NULL_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00003C': {'name': 'TLS_RSA_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00003D': {'name': 'TLS_RSA_WITH_AES_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00003E': {'name': 'TLS_DH_DSS_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00003F': {'name': 'TLS_DH_RSA_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000040': {'name': 'TLS_DHE_DSS_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000041': {'name': 'TLS_RSA_WITH_CAMELLIA_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000042': {'name': 'TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000043': {'name': 'TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000044': {'name': 'TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000045': {'name': 'TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000046': {'name': 'TLS_DH_Anon_WITH_CAMELLIA_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'000047': {'name': 'TLS_ECDH_ECDSA_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'000048': {'name': 'TLS_ECDH_ECDSA_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'000049': {'name': 'TLS_ECDH_ECDSA_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'00004A': {'name': 'TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00004B': {'name': 'TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00004C': {'name': 'TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000060': {'name': 'TLS_RSA_EXPORT1024_WITH_RC4_56_MD5', 'protocol': 'TLS', 'kx': 'RSA_EXPORT1024', 'au': 'RSA_EXPORT1024', 'enc': 'RC4_56', 'bits': '56', 'mac': 'MD5', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000061': {'name': 'TLS_RSA_EXPORT1024_WITH_RC2_CBC_56_MD5', 'protocol': 'TLS', 'kx': 'RSA_EXPORT1024', 'au': 'RSA_EXPORT1024', 'enc': 'RC2_CBC_56', 'bits': '56', 'mac': 'MD5', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000062': {'name': 'TLS_RSA_EXPORT1024_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA_EXPORT1024', 'au': 'RSA_EXPORT1024', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'EXPORT', 'enc_strength': 'LOW', 'overall_strength': 'EXPORT'},
'000063': {'name': 'TLS_DHE_DSS_EXPORT1024_WITH_DES_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'000064': {'name': 'TLS_RSA_EXPORT1024_WITH_RC4_56_SHA', 'protocol': 'TLS', 'kx': 'RSA_EXPORT1024', 'au': 'RSA_EXPORT1024', 'enc': 'RC4_56', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'EXPORT', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000065': {'name': 'TLS_DHE_DSS_EXPORT1024_WITH_RC4_56_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'RC4_56', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'000066': {'name': 'TLS_DHE_DSS_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'000067': {'name': 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000068': {'name': 'TLS_DH_DSS_WITH_AES_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000069': {'name': 'TLS_DH_RSA_WITH_AES_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00006A': {'name': 'TLS_DHE_DSS_WITH_AES_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00006B': {'name': 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00006C': {'name': 'TLS_DH_Anon_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00006D': {'name': 'TLS_DH_Anon_WITH_AES_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'000080': {'name': 'TLS_GOSTR341094_WITH_28147_CNT_IMIT', 'protocol': 'TLS', 'kx': 'VKO GOST R 34.10-94', 'au': 'VKO GOST R 34.10-94', 'enc': 'GOST28147', 'bits': '256', 'mac': 'IMIT_GOST28147', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000081': {'name': 'TLS_GOSTR341001_WITH_28147_CNT_IMIT', 'protocol': 'TLS', 'kx': 'VKO GOST R 34.10-2001', 'au': 'VKO GOST R 34.10-2001', 'enc': 'GOST28147', 'bits': '256', 'mac': 'IMIT_GOST28147', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000082': {'name': 'TLS_GOSTR341094_WITH_NULL_GOSTR3411', 'protocol': 'TLS', 'kx': 'VKO GOST R 34.10-94 ', 'au': 'VKO GOST R 34.10-94 ', 'enc': 'NULL', 'bits': '0', 'mac': 'HMAC_GOSTR3411', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'000083': {'name': 'TLS_GOSTR341001_WITH_NULL_GOSTR3411', 'protocol': 'TLS', 'kx': 'VKO GOST R 34.10-2001', 'au': 'VKO GOST R 34.10-2001', 'enc': 'NULL', 'bits': '0', 'mac': 'HMAC_GOSTR3411', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'000084': {'name': 'TLS_RSA_WITH_CAMELLIA_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000085': {'name': 'TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000086': {'name': 'TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000087': {'name': 'TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000088': {'name': 'TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000089': {'name': 'TLS_DH_Anon_WITH_CAMELLIA_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00008A': {'name': 'TLS_PSK_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'00008B': {'name': 'TLS_PSK_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00008C': {'name': 'TLS_PSK_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00008D': {'name': 'TLS_PSK_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00008E': {'name': 'TLS_DHE_PSK_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'00008F': {'name': 'TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000090': {'name': 'TLS_DHE_PSK_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000091': {'name': 'TLS_DHE_PSK_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000092': {'name': 'TLS_RSA_PSK_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'000093': {'name': 'TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000094': {'name': 'TLS_RSA_PSK_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000095': {'name': 'TLS_RSA_PSK_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000096': {'name': 'TLS_RSA_WITH_SEED_CBC_SHA', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'SEED_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000097': {'name': 'TLS_DH_DSS_WITH_SEED_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'SEED_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000098': {'name': 'TLS_DH_RSA_WITH_SEED_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'SEED_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'000099': {'name': 'TLS_DHE_DSS_WITH_SEED_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'SEED_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00009A': {'name': 'TLS_DHE_RSA_WITH_SEED_CBC_SHA', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'SEED_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00009B': {'name': 'TLS_DH_Anon_WITH_SEED_CBC_SHA', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'SEED_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00009C': {'name': 'TLS_RSA_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00009D': {'name': 'TLS_RSA_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00009E': {'name': 'TLS_DHE_RSA_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00009F': {'name': 'TLS_DHE_RSA_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000A0': {'name': 'TLS_DH_RSA_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000A1': {'name': 'TLS_DH_RSA_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000A2': {'name': 'TLS_DHE_DSS_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000A3': {'name': 'TLS_DHE_DSS_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000A4': {'name': 'TLS_DH_DSS_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000A5': {'name': 'TLS_DH_DSS_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000A6': {'name': 'TLS_DH_Anon_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'0000A7': {'name': 'TLS_DH_Anon_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'0000A8': {'name': 'TLS_PSK_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000A9': {'name': 'TLS_PSK_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000AA': {'name': 'TLS_DHE_PSK_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000AB': {'name': 'TLS_DHE_PSK_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000AC': {'name': 'TLS_RSA_PSK_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000AD': {'name': 'TLS_RSA_PSK_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000AE': {'name': 'TLS_PSK_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000AF': {'name': 'TLS_PSK_WITH_AES_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000B0': {'name': 'TLS_PSK_WITH_NULL_SHA256', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'0000B1': {'name': 'TLS_PSK_WITH_NULL_SHA384', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'0000B2': {'name': 'TLS_DHE_PSK_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000B3': {'name': 'TLS_DHE_PSK_WITH_AES_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000B4': {'name': 'TLS_DHE_PSK_WITH_NULL_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'0000B5': {'name': 'TLS_DHE_PSK_WITH_NULL_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'0000B6': {'name': 'TLS_RSA_PSK_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000B7': {'name': 'TLS_RSA_PSK_WITH_AES_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000B8': {'name': 'TLS_RSA_PSK_WITH_NULL_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'0000B9': {'name': 'TLS_RSA_PSK_WITH_NULL_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'0000BA': {'name': 'TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000BB': {'name': 'TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000BC': {'name': 'TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'CAMELLIA_128', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000BD': {'name': 'TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000BE': {'name': 'TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000BF': {'name': 'TLS_DH_Anon_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'0000C0': {'name': 'TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000C1': {'name': 'TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000C2': {'name': 'TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000C3': {'name': 'TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000C4': {'name': 'TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'0000C5': {'name': 'TLS_DH_Anon_WITH_CAMELLIA_256_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA256', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C001': {'name': 'TLS_ECDH_ECDSA_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00C002': {'name': 'TLS_ECDH_ECDSA_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'00C003': {'name': 'TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C004': {'name': 'TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C005': {'name': 'TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C006': {'name': 'TLS_ECDHE_ECDSA_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00C007': {'name': 'TLS_ECDHE_ECDSA_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'00C008': {'name': 'TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C009': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C00A': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C00B': {'name': 'TLS_ECDH_RSA_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00C00C': {'name': 'TLS_ECDH_RSA_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'00C00D': {'name': 'TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C00E': {'name': 'TLS_ECDH_RSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C00F': {'name': 'TLS_ECDH_RSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C010': {'name': 'TLS_ECDHE_RSA_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00C011': {'name': 'TLS_ECDHE_RSA_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'00C012': {'name': 'TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C013': {'name': 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C014': {'name': 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C015': {'name': 'TLS_ECDH_Anon_WITH_NULL_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'Anon', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00C016': {'name': 'TLS_ECDH_Anon_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'Anon', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'MEDIUM', 'overall_strength': 'MiM'},
'00C017': {'name': 'TLS_ECDH_Anon_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'Anon', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C018': {'name': 'TLS_ECDH_Anon_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'Anon', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C019': {'name': 'TLS_ECDH_Anon_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'Anon', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C01A': {'name': 'TLS_SRP_SHA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C01B': {'name': 'TLS_SRP_SHA_RSA_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C01C': {'name': 'TLS_SRP_SHA_DSS_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C01D': {'name': 'TLS_SRP_SHA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C01E': {'name': 'TLS_SRP_SHA_RSA_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C01F': {'name': 'TLS_SRP_SHA_DSS_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C020': {'name': 'TLS_SRP_SHA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C021': {'name': 'TLS_SRP_SHA_RSA_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C022': {'name': 'TLS_SRP_SHA_DSS_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'SRP', 'au': 'SHA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C023': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C024': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C025': {'name': 'TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C026': {'name': 'TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C027': {'name': 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C028': {'name': 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C029': {'name': 'TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C02A': {'name': 'TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C02B': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C02C': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C02D': {'name': 'TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C02E': {'name': 'TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C02F': {'name': 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C030': {'name': 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C031': {'name': 'TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'AES_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C032': {'name': 'TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'AES_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C033': {'name': 'TLS_ECDHE_PSK_WITH_RC4_128_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'RC4_128', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'MEDIUM', 'overall_strength': 'MEDIUM'},
'00C034': {'name': 'TLS_ECDHE_PSK_WITH_3DES_EDE_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C035': {'name': 'TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C036': {'name': 'TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C037': {'name': 'TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'AES_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C038': {'name': 'TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'AES_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C039': {'name': 'TLS_ECDHE_PSK_WITH_NULL_SHA ', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA ', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00C03A': {'name': 'TLS_ECDHE_PSK_WITH_NULL_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00C03B': {'name': 'TLS_ECDHE_PSK_WITH_NULL_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'NULL', 'bits': '0', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'NULL', 'overall_strength': 'NULL'},
'00C03C': {'name': 'TLS_RSA_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C03D': {'name': 'TLS_RSA_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C03E': {'name': 'TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C03F': {'name': 'TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C040': {'name': 'TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C041': {'name': 'TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C042': {'name': 'TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C043': {'name': 'TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C044': {'name': 'TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C045': {'name': 'TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C046': {'name': 'TLS_DH_Anon_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C047': {'name': 'TLS_DH_Anon_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C048': {'name': 'TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C049': {'name': 'TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C04A': {'name': 'TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C04B': {'name': 'TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C04C': {'name': 'TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C04D': {'name': 'TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C04E': {'name': 'TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C04F': {'name': 'TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C050': {'name': 'TLS_RSA_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C051': {'name': 'TLS_RSA_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C052': {'name': 'TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C053': {'name': 'TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C054': {'name': 'TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C055': {'name': 'TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C056': {'name': 'TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C057': {'name': 'TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C058': {'name': 'TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C059': {'name': 'TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C05A': {'name': 'TLS_DH_Anon_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA384', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C05B': {'name': 'TLS_DH_Anon_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C05C': {'name': 'TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C05D': {'name': 'TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C05E': {'name': 'TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C05F': {'name': 'TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C060': {'name': 'TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C061': {'name': 'TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C062': {'name': 'TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C063': {'name': 'TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C064': {'name': 'TLS_PSK_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C065': {'name': 'TLS_PSK_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C066': {'name': 'TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C067': {'name': 'TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C068': {'name': 'TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C069': {'name': 'TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C06A': {'name': 'TLS_PSK_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C06B': {'name': 'TLS_PSK_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C06C': {'name': 'TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C06D': {'name': 'TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C06E': {'name': 'TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'ARIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C06F': {'name': 'TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'ARIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C070': {'name': 'TLS_ECDHE_PSK_WITH_ARIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'ARIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C071': {'name': 'TLS_ECDHE_PSK_WITH_ARIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'ARIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C072': {'name': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C073': {'name': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C074': {'name': 'TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C075': {'name': 'TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C076': {'name': 'TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C077': {'name': 'TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C078': {'name': 'TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C079': {'name': 'TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C07A': {'name': 'TLS_RSA_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C07B': {'name': 'TLS_RSA_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C07C': {'name': 'TLS_DHE_RSA_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C07D': {'name': 'TLS_DHE_RSA_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C07E': {'name': 'TLS_DH_RSA_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C07F': {'name': 'TLS_DH_RSA_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'RSA', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C080': {'name': 'TLS_DHE_DSS_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C081': {'name': 'TLS_DHE_DSS_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'DSS', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C082': {'name': 'TLS_DH_DSS_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C083': {'name': 'TLS_DH_DSS_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'DSS', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C084': {'name': 'TLS_DH_Anon_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C085': {'name': 'TLS_DH_Anon_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DH', 'au': 'Anon', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'MiM', 'enc_strength': 'HIGH', 'overall_strength': 'MiM'},
'00C086': {'name': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C087': {'name': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'ECDSA', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C088': {'name': 'TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C089': {'name': 'TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'ECDSA', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C08A': {'name': 'TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C08B': {'name': 'TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'RSA', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C08C': {'name': 'TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C08D': {'name': 'TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'ECDH', 'au': 'RSA', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C08E': {'name': 'TLS_PSK_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C08F': {'name': 'TLS_PSK_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'CAMELLIA_256_GCM', 'bits': '128', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C090': {'name': 'TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C091': {'name': 'TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C092': {'name': 'TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'CAMELLIA_128_GCM', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C093': {'name': 'TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'CAMELLIA_256_GCM', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C094': {'name': 'TLS_PSK_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C095': {'name': 'TLS_PSK_WITH_CAMELLIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C096': {'name': 'TLS_DHE_PSK_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C097': {'name': 'TLS_DHE_PSK_WITH_CAMELLIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C098': {'name': 'TLS_RSA_PSK_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C099': {'name': 'TLS_RSA_PSK_WITH_CAMELLIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'PSK', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C09A': {'name': 'TLS_ECDHE_PSK_WITH_CAMELLIA_128_CBC_SHA256', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'CAMELLIA_128_CBC', 'bits': '128', 'mac': 'SHA256', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C09B': {'name': 'TLS_ECDHE_PSK_WITH_CAMELLIA_256_CBC_SHA384', 'protocol': 'TLS', 'kx': 'ECDHE', 'au': 'PSK', 'enc': 'CAMELLIA_256_CBC', 'bits': '256', 'mac': 'SHA384', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C09C': {'name': 'TLS_RSA_WITH_AES_128_CCM', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C09D': {'name': 'TLS_RSA_WITH_AES_256_CCM', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C09E': {'name': 'TLS_DHE_RSA_WITH_AES_128_CCM', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C09F': {'name': 'TLS_DHE_RSA_WITH_AES_256_CCM', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A0': {'name': 'TLS_RSA_WITH_AES_128_CCM_8', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A1': {'name': 'TLS_RSA_WITH_AES_256_CCM_8', 'protocol': 'TLS', 'kx': 'RSA', 'au': 'RSA', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A2': {'name': 'TLS_DHE_RSA_WITH_AES_128_CCM_8', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A3': {'name': 'TLS_DHE_RSA_WITH_AES_256_CCM_8', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'RSA', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A4': {'name': 'TLS_PSK_WITH_AES_128_CCM', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A5': {'name': 'TLS_PSK_WITH_AES_256_CCM', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A6': {'name': 'TLS_DHE_PSK_WITH_AES_128_CCM', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A7': {'name': 'TLS_DHE_PSK_WITH_AES_256_CCM', 'protocol': 'TLS', 'kx': 'DHE', 'au': 'PSK', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A8': {'name': 'TLS_PSK_WITH_AES_128_CCM_8', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0A9': {'name': 'TLS_PSK_WITH_AES_256_CCM_8', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'PSK', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0AA': {'name': 'TLS_PSK_DHE_WITH_AES_128_CCM_8', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'DHE', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0AB': {'name': 'TLS_PSK_DHE_WITH_AES_256_CCM_8', 'protocol': 'TLS', 'kx': 'PSK', 'au': 'DHE', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0AC': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_128_CCM', 'protocol': 'TLS', 'kx': 'ECDSA', 'au': 'PSK', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0AD': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_256_CCM', 'protocol': 'TLS', 'kx': 'ECDSA', 'au': 'PSK', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0AE': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8', 'protocol': 'TLS', 'kx': 'ECDSA', 'au': 'PSK', 'enc': 'AES_128', 'bits': '128', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00C0AF': {'name': 'TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8', 'protocol': 'TLS', 'kx': 'ECDSA', 'au': 'PSK', 'enc': 'AES_256', 'bits': '256', 'mac': 'CCM_8', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00FEFE': {'name': 'SSL_RSA_FIPS_WITH_DES_CBC_SHA', 'protocol': 'SSL', 'kx': 'RSA_FIPS', 'au': 'RSA_FIPS', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'00FEFF': {'name': 'SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA', 'protocol': 'SSL', 'kx': 'RSA_FIPS', 'au': 'RSA_FIPS', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00FFE0': {'name': 'SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA', 'protocol': 'SSL', 'kx': 'RSA_FIPS', 'au': 'RSA_FIPS', 'enc': '3DES_EDE_CBC', 'bits': '168', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'HIGH', 'overall_strength': 'HIGH'},
'00FFE1': {'name': 'SSL_RSA_FIPS_WITH_DES_CBC_SHA', 'protocol': 'SSL', 'kx': 'RSA_FIPS', 'au': 'RSA_FIPS', 'enc': 'DES_CBC', 'bits': '56', 'mac': 'SHA', 'kxau_strength': 'HIGH', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'010080': {'name': 'SSL2_RC4_128_WITH_MD5', 'protocol': 'SSL2', 'kx': 'RSA', 'au': 'RSA', 'enc': 'RC4_128', 'bits': '128', 'mac': 'MD5', 'kxau_strength': 'LOW', 'enc_strength': 'MEDIUM', 'overall_strength': 'LOW'},
'020080': {'name': 'SSL2_RC4_128_EXPORT40_WITH_MD5', 'protocol': 'SSL2', 'kx': 'RSA', 'au': 'RSA', 'enc': 'RC4_128_EXPORT40', 'bits': '40', 'mac': 'MD5', 'kxau_strength': 'LOW', 'enc_strength': 'EXPORT', 'overall_strength': 'EXPORT'},
'030080': {'name': 'SSL2_RC2_CBC_128_CBC_WITH_MD5', 'protocol': 'SSL2', 'kx': 'RSA', 'au': 'RSA', 'enc': 'RC2_CBC_128_CBC', 'bits': '128', 'mac': 'MD5', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'040080': {'name': 'SSL2_RC2_CBC_128_CBC_WITH_MD5', 'protocol': 'SSL2', 'kx': 'RSA', 'au': 'RSA', 'enc': 'RC2_CBC_128_CBC', 'bits': '128', 'mac': 'MD5', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'050080': {'name': 'SSL2_IDEA_128_CBC_WITH_MD5', 'protocol': 'SSL2', 'kx': 'RSA', 'au': 'RSA', 'enc': 'IDEA_128_CBC', 'bits': '128', 'mac': 'MD5', 'kxau_strength': 'LOW', 'enc_strength': 'HIGH', 'overall_strength': 'LOW'},
'060040': {'name': 'SSL2_DES_64_CBC_WITH_MD5', 'protocol': 'SSL2', 'kx': 'RSA', 'au': 'RSA', 'enc': 'DES_64_CBC', 'bits': '64', 'mac': 'MD5', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'0700C0': {'name': 'SSL2_DES_192_EDE3_CBC_WITH_MD5', 'protocol': 'SSL2', 'kx': 'RSA', 'au': 'RSA', 'enc': 'DES_192_EDE3_CBC', 'bits': '192', 'mac': 'MD5', 'kxau_strength': 'LOW', 'enc_strength': 'HIGH', 'overall_strength': 'LOW'},
'080080': {'name': 'SSL2_RC4_64_WITH_MD5', 'protocol': 'SSL2', 'kx': 'RSA', 'au': 'RSA', 'enc': 'RC4_64', 'bits': '64', 'mac': 'MD5', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'800001': {'name': 'PCT_SSL_CERT_TYPE | PCT1_CERT_X509', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'800003': {'name': 'PCT_SSL_CERT_TYPE | PCT1_CERT_X509_CHAIN', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'810001': {'name': 'PCT_SSL_HASH_TYPE | PCT1_HASH_MD5', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'810003': {'name': 'PCT_SSL_HASH_TYPE | PCT1_HASH_SHA', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'820001': {'name': 'PCT_SSL_EXCH_TYPE | PCT1_EXCH_RSA_PKCS1', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'830004': {'name': 'PCT_SSL_CIPHER_TYPE_1ST_HALF | PCT1_CIPHER_RC4', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'842840': {'name': 'PCT_SSL_CIPHER_TYPE_2ND_HALF | PCT1_ENC_BITS_40 | PCT1_MAC_BITS_128', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'848040': {'name': 'PCT_SSL_CIPHER_TYPE_2ND_HALF | PCT1_ENC_BITS_128 | PCT1_MAC_BITS_128', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'8F8001': {'name': 'PCT_SSL_COMPAT | PCT_VERSION_1', 'protocol': 'PCT', 'kx': '', 'au': '', 'enc': '', 'bits': '', 'mac': '', 'kxau_strength': 'LOW', 'enc_strength': 'LOW', 'overall_strength': 'LOW'},
'0000FF': {'name': 'TLS_EMPTY_RENEGOTIATION_INFO_SCSV'},
'00CC13': {'name': 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256'},
'00CC14': {'name': 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256'},
'00CC15': {'name': 'TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256'},
'005A5A': {'name': 'RSERVED(GREASE)'},
'001301': {'name': 'TLS_AES_128_GCM_SHA256'},
'001302': {'name': 'TLS_AES_256_GCM_SHA384'},
'001303': {'name': 'TLS_CHACHA20_POLY1305_SHA256'},
'00CCA9': {'name': 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256'},
'00CCA8': {'name': 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256'}
}

TLS = {
2: {'name': 'SSLv2.0'},
768: {'name': 'SSLv3.0'},
769: {'name': 'TLSv1.0'},
770: {'name': 'TLSv1.1'},
771: {'name': 'TLSv1.2'},
772: {'name': 'TLSv1.3'}
}

import subprocess
import os
import math
from netaddr import IPNetwork
import requests
import sys
import re

def most_frequent(List): 
    return max(set(List), key = List.count) 

web_server ='ramo.cs.uiowa.edu'
server_file = 'server_side/{}.pcap'.format(sys.argv[1])
client_file = 'client_side/{}.pcapng'.format(sys.argv[1])
time_adjust = 2
dest_server='10.255.3.19'
src_browser='10.42.0.80/24'
print("Browser = {}".format(sys.argv[1]))

# process server packets
output = os.popen("tshark -V  -Y \"ssl\" -r {} -e frame.time_epoch  -T fields".format(server_file)).read()
outputList=output.splitlines()
timefirst = math.floor(float(outputList[0]))-time_adjust
timelast = math.floor(float(outputList[len(outputList)-1]))+time_adjust
print("First frame time in server = {}".format(timefirst))
print("Last frame time in server= {}".format(timelast))
output = os.popen("tshark -V  -Y \"ssl\" -r {}".format(server_file)).read()
serverpackets = output.split("Frame \\d+:")
# for serverp in serverpackets:
#     print(serverp)

# process client packets
cmd = "tshark -V -Y \"ssl && frame.time_epoch >= {} && frame.time_epoch <= {}\" -r {}".format(math.floor(float(timefirst)), math.ceil(float(timelast)), client_file)
output = os.popen(cmd).read()
clientpackets = output.split("Frame \\d+:")
# for clientp in clientpackets:
#     print(clientp)

def ProxyByvolume():
    StcpStreams = os.popen("tshark -V -Y \"ssl.handshake.type==1\" -r {} -e ip.src -e tcp.stream  -T fields".format(server_file)).read()
    StcpStreamsIP = StcpStreams.splitlines()
    for tcpStreamIP in StcpStreamsIP:
        tcpStream=tcpStreamIP.split("\t")
        StcpStreams = os.popen("tshark -z \"follow,tcp,raw, {}\" -r {}|awk \"f;/Node 1:.*/{{f=1}}\"".format(int(tcpStream[1]), server_file)).read()
        clientTcp=0
        serverTcp=0
        StcpStreams=StcpStreams.splitlines()
        for g in StcpStreams:
            if (g.startswith("\t")):
                serverTcp=serverTcp+((len(g)-2)/2)
            else:
                clientTcp=clientTcp+(len(g)/2)
        print("probable proxy IP {}/{}, proxy to server tcp size = {}, server to proxy tcp size {}".format(tcpStream[0],tcpStream[1], clientTcp, serverTcp))

    print("\n")
    CtcpStreams = os.popen("tshark -V -Y \"frame.time_epoch >= {} && frame.time_epoch <= {}\" -r {} -e ip.dst -e tcp.stream -T fields".format(math.floor(float(timefirst)), math.ceil(float(timelast)),client_file)).read()
    CtcpStreamsIP = CtcpStreams.splitlines()
    CtcpStreamsIP=set(CtcpStreamsIP)
    print(CtcpStreamsIP)
    for tcpStreamIP in CtcpStreamsIP:
        tcpStream=tcpStreamIP.split("\t")
        if (tcpStream[1] != ''):
            CtcpStreams = os.popen("tshark -z \"follow,tcp,raw, {}\" -r {}|awk \"f;/Node 1:.*/{{f=1}}\"".format(int(tcpStream[1]), client_file)).read()
            clientTcp=0
            proxyTCP=0
            CtcpStreams=CtcpStreams.splitlines()
            for g in CtcpStreams:
                if (g.startswith("\t")):
                    proxyTCP=proxyTCP+((len(g)-2)/2)
                else:
                    clientTcp=clientTcp+(len(g)/2)
            print("probable proxy IP {}/{}, browser to proxy tcp size = {}, proxy to browser tcp size {}".format(tcpStream[0],tcpStream[1],clientTcp, proxyTCP))




# determine proxy address
output = os.popen("tshark -V  -Y \"ssl && ip.dst == {}\" -r {} -e ip.src  -T fields".format(dest_server, server_file)).read()
serverProxy=output.splitlines()[0]
#print(serverProxy)

cmd = "tshark -V -Y \"ssl && ip.src == {} && frame.time_epoch >= {} && frame.time_epoch <= {}\" -r {} -e ip.dst  -T fields".format(src_browser, math.floor(float(timefirst)), math.ceil(float(timelast)), client_file)
output = os.popen(cmd).read()
clientProxy=output.splitlines()
#print(clientProxy)
proxyserver=[]
clientp=''
serverp=''
flag='false'
for ip in clientProxy:
    if (flag == 'true'):
        break
    if IPNetwork(ip+'/32') == IPNetwork(serverProxy+'/32'):
        proxyserver.append(ip+'/32')
        print("\nproxyAddress = {}".format(proxyserver))
        clientp=ip
        serverp=ip
        flag = 'true'
    elif IPNetwork(ip+'/31') == IPNetwork(serverProxy+'/31'):
        proxyserver.append(ip+'/31')
        proxyserver.append(serverProxy+'/31')
        print("\nproxyAddress = {}".format(proxyserver))
        clientp=ip
        serverp=serverProxy
        flag = 'true'
    elif IPNetwork(ip+'/30') == IPNetwork(serverProxy+'/30'):
        proxyserver.append(ip+'/30')
        proxyserver.append(serverProxy+'/30')
        print("\nproxyAddress = {}".format(proxyserver))
        clientp=ip
        serverp=serverProxy
        flag = 'true'
    elif IPNetwork(ip+'/29') == IPNetwork(serverProxy+'/29'):
        proxyserver.append(ip+'/29')
        proxyserver.append(serverProxy+'/29')
        print("\nproxyAddress = {}".format(proxyserver))
        clientp=ip
        serverp=serverProxy
        flag = 'true'
    elif IPNetwork(ip+'/28') == IPNetwork(serverProxy+'/28'):
        proxyserver.append(ip+'/28')
        proxyserver.append(serverProxy+'/28')
        print("\nproxyAddress = {}".format(proxyserver))
        clientp=ip
        serverp=serverProxy
        flag = 'true'
    elif IPNetwork(ip+'/27') == IPNetwork(serverProxy+'/27'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/27')
                proxyserver.append(serverProxy+'/27')
                print("\nproxyAddress = {}".format(proxyserver))
                clientp=ip
                serverp=serverProxy
                # print("probable proxy from server traces " + str(geo_data2))
                # print("proxy from cleint traces "+ str(geo_data1))
                flag='true'
    elif IPNetwork(ip+'/26') == IPNetwork(serverProxy+'/26'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/26')
                proxyserver.append(serverProxy+'/26')
                print("\nproxyAddress = {}".format(proxyserver))
                clientp=ip
                serverp=serverProxy
                # print("probable proxy from server traces " + str(geo_data2))
                # print("proxy from cleint traces "+ str(geo_data1))
                flag='true'
    elif IPNetwork(ip+'/25') == IPNetwork(serverProxy+'/25'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/25')
                proxyserver.append(serverProxy+'/25')
                print("\nproxyAddress = {}".format(proxyserver))
                clientp=ip
                serverp=serverProxy
                flag='true'
    elif IPNetwork(ip+'/24') == IPNetwork(serverProxy+'/24'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/24')
                proxyserver.append(serverProxy+'/24')
                print("\nproxyAddress = {}".format(proxyserver))
                clientp=ip
                serverp=serverProxy
                flag='true'
    elif IPNetwork(ip+'/23') == IPNetwork(serverProxy+'/23'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/23')
                proxyserver.append(serverProxy+'/23')
                print("\nproxyAddress = {}".format(proxyserver))
                clientp=ip
                serverp=serverProxy
                flag='true'
    elif IPNetwork(ip+'/22') == IPNetwork(serverProxy+'/22'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        #print(geo_data1)
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        #print(geo_data2)
        # if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
        #     and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']): ---------------------for uc mini
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/22')
                proxyserver.append(serverProxy+'/22')
                print("\nproxyAddress = {}".format(proxyserver))
                clientp=ip
                serverp=serverProxy
                flag='true'
    elif IPNetwork(ip+'/21') == IPNetwork(serverProxy+'/21'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/21')
                proxyserver.append(serverProxy+'/21')
                print("\nproxyAddress = {}".format(proxyserver))
                clientp=ip
                serverp=serverProxy
                flag='true'
    elif IPNetwork(ip+'/20') == IPNetwork(serverProxy+'/20'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/20')
                proxyserver.append(serverProxy+'/20')
                print("\nproxyAddress = {}".format(proxyserver))
                clientp=ip
                serverp=serverProxy
                flag='true'
    elif IPNetwork(ip+'/19') == IPNetwork(serverProxy+'/19'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/19')
                proxyserver.append(serverProxy+'/19')
                print("\nproxyAddress = {}".format(proxyserver))
                ProxyByvolume()
                flag='true'
    elif IPNetwork(ip+'/18') == IPNetwork(serverProxy+'/18'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/18')
                proxyserver.append(serverProxy+'/18')
                print("\nproxyAddress = {}".format(proxyserver))
                ProxyByvolume()
                flag='true'
    elif IPNetwork(ip+'/17') == IPNetwork(serverProxy+'/17'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/17')
                proxyserver.append(serverProxy+'/17')
                print("\nproxyAddress = {}".format(proxyserver))
                ProxyByvolume()
                flag='true'
    elif IPNetwork(ip+'/16') == IPNetwork(serverProxy+'/16'):
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data1 = geo_request.json()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + serverProxy + '.json'
        geo_request = requests.get(geo_request_url)
        geo_data2 = geo_request.json()
        if (geo_data1['asn'] == geo_data2['asn'] and geo_data1['region'] == geo_data2['region'] 
            and geo_data1['city'] == geo_data2['city'] and geo_data1['country'] == geo_data2['country']):
                proxyserver.append(ip+'/16')
                proxyserver.append(serverProxy+'/16')
                print("\nproxyAddress = {}".format(proxyserver))
                ProxyByvolume()
                flag='true'

if (flag=='false'):
    ProxyByvolume()
    print("couldn't determine proxy address")

#tunnel or interception
Class='0'
output = os.popen("tshark -V -Y \"ssl.handshake.type==11 && ip.src=={}\" -r {}".format(clientp, client_file)).read()
flag = re.search("id-at-commonName=ramo.cs.uiowa.edu", output)
if flag:
    Class='1'
    print('\nHTTP tunneling')
else:
    Class='2'
    print('\nInterception')

cmd=''
# determine offered ciphersuite from client hellos
if(Class=='1'):
    cmd = "tshark -V -Y \"ssl.handshake.type==1 && ip.dst=={} && frame.time_epoch >= {} && frame.time_epoch <= {}\" -r {} -e ssl.handshake.ciphersuite   -T fields".format(clientp,math.floor(float(timefirst)), math.ceil(float(timelast)), client_file)
elif(Class=='2'):
    cmd = "tshark -V -Y \"ssl.handshake.type==1 && ip.dst=={}\" -r {} -e ssl.handshake.ciphersuite   -T fields".format(clientp, client_file)
output = os.popen(cmd).read()
outputList1=output.splitlines()[0].split(',')
ciphertoProxyList = []
print("\ncipher offered to proxy = ")
for f in outputList1:
    ciphertoProxy="{:06x}".format(int(f)).upper()
    ciphertoProxy = cipher_suites.get(ciphertoProxy, ciphertoProxy)
    ciphertoProxyList.append(ciphertoProxy)
    print(ciphertoProxy)

output = os.popen("tshark -V  -Y \"ssl.handshake.type==1\" -r {} -e ssl.handshake.ciphersuite   -T fields".format(server_file)).read()
outputList1=output.splitlines()[0].split(',')
print("\ncipher offered to server = ")
ciphertoServerList = []
for f in outputList1:
    ciphertoServer="{:06x}".format(int(f)).upper()
    ciphertoServer = cipher_suites.get(ciphertoServer, ciphertoServer)
    ciphertoServerList.append(ciphertoServer)
    print(ciphertoServer)

# determine selected ciphersuite from server hellos
output = os.popen("tshark -V  -Y \"ssl.handshake.type==2\" -r {} -e ssl.handshake.ciphersuite   -T fields".format(server_file)).read()
cipherfromSever= "{:06x}".format(int(output.splitlines()[0])).upper()
cipherfromSever = cipher_suites.get(cipherfromSever, cipherfromSever)
print("\ncipher selected by server = " + str(cipherfromSever))

cmd=''
if(Class=='1'):
    cmd = "tshark -V -Y \"ssl.handshake.type==2 && ip.src=={} && frame.time_epoch >= {} && frame.time_epoch <= {}\" -r {} -e ssl.handshake.ciphersuite   -T fields".format(clientp,math.floor(float(timefirst)), math.ceil(float(timelast)), client_file)
elif(Class=='2'):
    cmd = "tshark -V -Y \"ssl.handshake.type==2 && ip.src=={}\" -r {} -e ssl.handshake.ciphersuite   -T fields".format(clientp, client_file)
output = os.popen(cmd).read()
cipherfromProxy= "{:06x}".format(int(output.splitlines()[0])).upper()
cipherfromProxy = cipher_suites.get(cipherfromProxy, cipherfromProxy)
print("cipher selected by proxy = " + str(cipherfromProxy))

# #tls_version client hellos
cmd=''
if(Class=='1'):
    cmd = "tshark -V -Y \"ssl.handshake.type==1 && ip.dst=={} && frame.time_epoch >= {} && frame.time_epoch <= {}\" -r {} -e ssl.handshake.version   -T fields".format(clientp,math.floor(float(timefirst)), math.ceil(float(timelast)), client_file)
elif(Class=='2'):
    cmd = "tshark -V -Y \"ssl.handshake.type==1 && ip.dst=={}\" -r {} -e ssl.handshake.version   -T fields".format(clientp, client_file)
output = os.popen(cmd).read()
CtlsToProxy= int(output.splitlines()[0], 0)
CtlsToProxy = TLS.get(CtlsToProxy, CtlsToProxy)
print("\nTLS offered by client to proxy = " + CtlsToProxy['name'])

output = os.popen("tshark -V  -Y \"ssl.handshake.type==1\" -r {} -e ssl.handshake.version   -T fields".format(server_file)).read()
CtlsToServer= int(output.splitlines()[0], 0)
CtlsToServer = TLS.get(CtlsToServer, CtlsToServer)
print("TLS offered by proxy to server = " + CtlsToServer['name'])

# #tls_version server hellos
output = os.popen("tshark -V  -Y \"ssl.handshake.type==2\" -r {} -e ssl.handshake.version   -T fields".format(server_file)).read()
StlsToProxy= int(output.splitlines()[0], 0)
StlsToProxy = TLS.get(StlsToProxy, StlsToProxy)
print("TLS selected by server to proxy = " + StlsToProxy['name'])

cmd=''
if(Class=='1'):
    cmd = "tshark -V -Y \"ssl.handshake.type==2 && ip.src=={} && frame.time_epoch >= {} && frame.time_epoch <= {}\" -r {} -e ssl.handshake.version   -T fields".format(clientp,math.floor(float(timefirst)), math.ceil(float(timelast)), client_file)
elif(Class=='2'):
    cmd = "tshark -V -Y \"ssl.handshake.type==2 && ip.src=={}\" -r {} -e ssl.handshake.version   -T fields".format(clientp, client_file)
StlsToClient= int(output.splitlines()[0], 0)
StlsToClient = TLS.get(StlsToClient, StlsToClient)
print("TLS selected by proxy to client = " + StlsToClient['name'])

#sha and key size server to proxy cert
output = os.popen("tshark -Y\"ssl.handshake.type==11\" -r {} -T pdml".format(server_file)).read()
regex = re.compile("signature \((.*)\)")
SSHA = regex.search(output).group(1)
print('\nSignature Hash Algo from server trace = {}'.format(SSHA))

regex = re.compile("modulus:.*size=\"(\\d+)\".*")
Srsa_key_size = int(regex.search(output).group(1), 10) * 8
print('RSA key size from server trace = {} bit'.format(Srsa_key_size))

#sha and key size proxy to browser cert
cmd=''
if(Class=='1'):
    cmd = "tshark -V -Y \"ssl.handshake.type==11 && frame.time_epoch >= {} && frame.time_epoch <= {}\" -r {} -T pdml".format(math.floor(float(timefirst)), math.ceil(float(timelast)), client_file)
elif(Class=='2'):
    cmd = "tshark -Y\"ssl.handshake.type==11 && ip.src=={}\" -r {} -T pdml".format(clientp, client_file)
output = os.popen(cmd).read()
regex = re.compile("signature \((.*)\)")
CSHA = regex.search(output).group(1)
print('Signature Hash Algo from client trace = {}'.format(CSHA))

regex = re.compile("modulus:.*size=\"(\\d+)\".*")
Crsa_key_size = int(regex.search(output).group(1), 10) * 8
print('RSA key size from client trace = {} bit'.format(Crsa_key_size))