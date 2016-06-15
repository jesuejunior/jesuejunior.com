DJANGO_LOGLEVEL (DEBUG|INFO|ERROR|WARNING|CRITICAL)
DJANGO_LOG %{DJANGO_LOGLEVEL:log_level}\s+%{TIMESTAMP_ISO8601:log_timestamp}\s+%{TZ:log_tz}\s+%{NOTSPACE:logger}\s+%{WORD:module}\s+%{POSINT:proc_id}\s+%{GREEDYDATA:content}

logstash filter

filter {
     if [type] == "django" {
        grok {
             match => ["message", "%{DJANGO_LOG}" ]
        }

        date {
            match => [ "timestamp", "ISO8601", "YYYY-MM-dd HH:mm:ss,SSS"]
            target => "@timestamp"
        }
     }
}
