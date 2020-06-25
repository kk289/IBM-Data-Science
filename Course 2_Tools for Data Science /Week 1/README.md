# Open Source Tools for Data Science
# Week 1

## Language of Data Science

Most popular programming langaugages:   
- Python
- R
- SQL

Other:    
- Scala
- Java
- C++
- Julia
- Javascript
- PHP
- Go
- Ruby
- Visual Basic

What are the roles we can apply for people who are interested in getting involved in data science?
- Business Analyst
- Database Engineer
- Data Analyst
- Data Engineer
- Data Scientist
- Research Scientist
- Software Engineer
- Statistician
- Product Manager
- Project Manager and many more.

### Introduction to Python

- According to the 2019 Kaggle Data Science and Machine Learning Survey, 75% of the over 10,000 respondents from around the world reported that they use Python on a regular basis.
- Python is useful for many situations, including data science, AI and machine learning, web development, and IoT devices like the Raspberry Pi.
- Large organizations that use Python heavily include IBM, Wikipedia, Google, Yahoo!, CERN, NASA, Facebook, Amazon, Instagram, Spotify, and Reddit.
- For data science, we can use Python's scientific computing libraries such as Pandas, NumPy, SciPy, and Matplotlib.
- For artificial intelligence, it has TensorFlow, PyTorch, Keras, and Scikit-learn.
- Python can also be used for Natural Language Processing (NLP) using the Natural Language Toolkit (NLTK).

### Introduction to R

- Like Python, R is free to use, but it's a GNU project - instead of being open source, it's actually free software.
- It's most often used by statisticians, mathematicians, and data miners for developing statistical software, graphing, and data analysis. 
- R is popular in academia but companies that use R include IBM, Google, Facebook, Microsoft, Bank of America, Ford, TechCrunch, Uber, and Trulia. 
- R has become the world’s largest repository of statistical knowledge.
- As of 2018, R has more than 15,000 publicly released packages, making it possible to conduct complex exploratory data analysis.
- R integrates well with other computer languages, such as C++, Java, C, .Net, and Python.
- Common mathematical operations such as matrix multiplication work straight out of the box.
- R has stronger object-oriented programming facilities than most statistical computing languages

### Introduction to SQL (Structured Query Language)

- It's much older than Python and R, by about 20 years, having first appeared in 1974.
- SQL was developed at IBM! This language is useful in handling structured data; that is, the data incorporating relations among entities and variables.
- SQL was designed for managing data in relational databases
- The SQL language is subdivided into several language elements, including clauses, expressions, predicates, queries, and statements
- There are many different SQL databases available, including MySQL, IBM Db2, PostgreSQL, Apache OpenOffice Base, SQLite, Oracle, MariaDB, Microsoft SQL Server, and more. 

### Other languages

- Scala, Java, C++, and Julia are probably the most traditional data science languages
- JavaScript, PHP, Go, Ruby, Visual Basic, and others have all found their place in the data science community as well!

#### JAVA

- Java is a tried-and-true general-purpose object oriented programming language. 
- It's been widely adopted in the enterprise space and is designed to be fast and scalable.
- Java applications are compiled to bytecode and run on the Java Virtual Machine, or "JVM."
- Some notable data science tools built with Java include Weka, for data mining;
- Java-ML, which is a machine learning library; 
- Apache MLlib, which makes machine learning scalable; 
- Deeplearning4j, which is for deep learning.
- Apache Hadoop is another Java-built application. It manages data processing and storage for big data applications running in clustered systems.

#### Scala

- Scala is a general-purpose programming language that provides support for functional programming and a strong static type system.
- Many of the design decisions in the construction of the Scala language were made to address criticisms of Java.
- Scala is also interoperable with Java, as it runs on the JVM.
- The name "Scala" is a combination of "scalable" and "language." This language is designed to grow along with the demands of its users. 
- For data science, the most popular program built using Scala is Apache Spark. 
- Spark is a fast and general-purpose cluster computing system. It provides APIs that make parallel jobs easy to write, and an optimized engine that supports general computation graphs.
- Spark includes Shark, which is a query engine; 
- MLlib, for machine learning; 
- GraphX, for graph processing;
- Spark Streaming. Apache Spark was designed to be faster than Hadoop.

#### C++ 

- C++ is a general-purpose programming language. It is an extension of the C programming language, or "C with Classes.”
- C++ improves processing speed, enables system programming, and provides broader control over the software application.
- For data science, a popular deep learning library for dataflow called TensorFlow was built with C++. 
- MongoDB, a NoSQL database for big data management, was built with C++. Caffe is a deep learning algorithm repository built with C++, with Python and MATLAB bindings.

#### JavaScript

- JavaScript is a general-purpose language that extended beyond the browser with the creation of Node.js and other server-side approaches. 
- Javascript is NOT related to the Java language.
- For data science, the most popular implementation is undoubtedly TensorFlow.js. 
- TensorFlow.js makes machine learning and deep learning possible in Node.js as well as in the browser.
- TensorFlow.js was also adopted by other open source libraries, including brain.js and machinelearn.js. 
- The R-js project is another great implementation of JavaScript for data science. 
- R-js has re-written linear algebra specifications from the R Language into Typescript.
- Typescript is a superset of JavaScript.

#### Julia

- Julia was designed at MIT for high-performance numerical analysis and computational science.
- It provides speedy development like Python or R, while producing programs that run as fast as C or Fortran programs. 
- Julia is compiled, which means that the code is executed directly on the processor as executable code; it calls C, Go, Java, MATLAB, R, Fortran, and Python libraries; and has refined parallelism.
- The Julia language is relatively new, having been written in 2012, but it has a lot of promise for future impact on the data science industry.
- JuliaDB is a particularly useful application of Julia for data science.
- It's a package for working with large persistent data sets.

## Data Science Tools

### Categories of Data Science Tools

- Data Management is the process of persisting and retrieving data.
- Data Integration and Transformation, often referred to as Extract, Transform, and Load, or “ETL,” is the process of retrieving data from remote data management systems. 
- Transforming data and loading it into a local data management system is also part of Data Integration and Transformation.
- Data Visualization is part of an initial data exploration process, as well as being part of a final deliverable.
- Model Building is the process of creating a machine learning or deep learning model using an appropriate algorithm with a lot of data. 
- Model deployment makes such a machine learning or deep learning model available to third-party applications. 
- Model monitoring and assessment ensures continuous performance quality checks on the deployed models.
- Data asset management brings the same versioning and collaborative components to data. Data asset management also supports replication, backup, and access right management.
- Development environments, commonly known as Integrated Development Environments, or “IDEs”, are tools that help the data scientist to implement, execute, test, and deploy their work. 
- Execution environments are tools where data preprocessing, model training, and deployment take place.

### Open Source Tools for Data Science: Part 1

- The most widely used open source data management tools are relational databases:
    - MySQL and PostgreSQL; 
    - NoSQL databases such as MongoDB Apache CouchDB, and Apache Cassandra;
    - File-based tools such as the Hadoop File System or Cloud File systems like Ceph.
- Elasticsearch is mainly used for storing text data and creating a search index for fast document retrieval.
- The task of data integration and transformation in the classic data warehousing world is called ETL, which stands for “extract, transform, and load.
- The most widely used open source data integration and transformation tools: 
    - Apache AirFlow, originally created by AirBNB; 
    - KubeFlow, which enables you to execute data science pipelines on top of Kubernetes; 
    - Apache Kafka, which originated from LinkedIn; 
    - Apache Nifi, which delivers a very nice visual editor; 
    - Apache SparkSQL (which enables to use ANSI SQL and scales up to compute clusters of 1000s of nodes),
    - NodeRED, which also provides a visual editor. NodeRED consumes so little in resources that it even runs on small devices like a Raspberry Pi
-  The most widely used open source data visualization tools:
    - Hue, which can create visualizations from SQL queries.
    - Kibana, a data exploration and visualization web application, is limited to Elasticsearch.
    - Finally, Apache Superset is a data exploration and visualization web application.
- Model deployment is extremely important. Once we’ve created a machine learning model capable of predicting some key aspects of the future, we should make that model consumable by other developers and turn it into an API:
    - Apache PredictionIO currently only supports Apache Spark ML models for deployment, but support for all sorts of other libraries is on the roadmap.
    - Seldon is an interesting product since it supports nearly every framework, including TensorFlow, Apache SparkML, R, and scikit-learn.
    -  Seldon can run on top of Kubernetes and Redhat OpenShift.
  