def extract_skills(text):
    skill_keywords = [
        # Programming Languages
        "python", "java", "c++", "c#", "javascript", "typescript", "golang", "rust", "php", "ruby", "scala", "kotlin", "swift", "objectivec", "perl", "r", "matlab", "groovy", "lua", "vb.net",
        
        # Web Development
        "html", "css", "react", "vue", "angular", "nodejs", "express", "django", "flask", "fastapi", "spring", "laravel", "aspnet", "asp.net", "nextjs", "nuxt", "svelte", "webpack", "gulp", "grunt",
        
        # Databases
        "sql", "mysql", "postgresql", "mongodb", "oracle", "redis", "cassandra", "elasticsearch", "dynamodb", "mariadb", "sqlite", "firebase", "realm", "neo4j", "couchdb",
        
        # Data Science & Machine Learning
        "machine learning", "deep learning", "data science", "nlp", "computer vision", "artificial intelligence", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "keras", "opencv", "nltk", "spacy", "xgboost", "lightgbm", "catboost",
        
        # Data Visualization
        "power bi", "tableau", "power bi desktop", "looker", "grafana", "kibana", "matplotlib", "seaborn", "plotly", "d3.js",
        
        # Cloud & DevOps
        "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "jenkins", "gitlab ci", "github actions", "terraform", "ansible", "cloudformation", "heroku", "digitalocean", "openshift",
        
        # Version Control & Collaboration
        "git", "github", "gitlab", "bitbucket", "svn", "mercurial", "jira", "confluence", "slack",
        
        # Big Data
        "hadoop", "spark", "hive", "pig", "mapreduce", "kafka", "flink", "storm",
        
        # Mobile Development
        "android", "ios", "react native", "flutter", "xamarin", "cordova", "ionic",
        
        # APIs & Protocols
        "rest", "graphql", "soap", "mqtt", "http", "https", "websocket", "json", "xml",
        
        # Testing & QA
        "junit", "pytest", "selenium", "cypress", "postman", "jmeter", "testng", "mocha", "jasmine", "jest", "rspec",
        
        # Office & Productivity
        "excel", "word", "powerpoint", "outlook", "sheets", "docs", "slides", "notion", "asana", "monday.com",
        
        # Content Management & Design
        "wordpress", "drupal", "joomla", "wix", "shopify", "adobe xd", "figma", "sketch", "invision", "photoshop", "illustrator", "blender",
        
        # Operating Systems
        "linux", "windows", "macos", "ubuntu", "debian", "centos", "fedora",
        
        # Additional Technical Skills
        "api", "rest api", "microservices", "agile", "scrum", "kanban", "ci/cd", "linux", "bash", "shell scripting", "powershell", "regex", "json", "yaml", "markdown", "vim", "virtualbox", "vmware", "mqtt", "grpc", "protobuf", "message queue", "rabbitmq", "zeromq",
        
        # Cybersecurity
        "penetration testing", "pentesting", "ethical hacking", "vulnerability assessment", "security audit", "network security", "application security", "web security", "cryptography", "encryption", "decryption", "ssl/tls", "ssh", "vpn", "firewall", "ids", "ips", "intrusion detection", "intrusion prevention", "siem", "security information and event management", "incident response", "malware analysis", "reverse engineering", "burp suite", "metasploit", "wireshark", "nmap", "aircrack", "hashcat", "sqlmap", "nikto", "owasp", "ceh", "ccna security", "cissp", "oscp", "security+", "zero trust", "secure coding", "code review", "static analysis", "dynamic analysis", "vulnerability scanning", "threat modeling", "risk assessment", "access control", "authentication", "authorization", "multi factor authentication", "mfa", "biometric", "oauth", "saml", "ldap", "active directory", "iam", "identity and access management", "password hashing", "salting", "privilege escalation", "lateral movement", "data exfiltration", "ddos", "cross site scripting", "xss", "sql injection", "csrf", "phishing", "social engineering", "security awareness", "compliance", "pci dss", "hipaa", "gdpr", "iso 27001", "nist", "cis controls"
    ]

    found_skills = []

    for skill in skill_keywords:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))
