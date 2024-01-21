# System Design Notebook

# 1. Concepts

## 1.1 API Gateway
An API Gateway is a centralized entry point that acts as a single point of contact for multiple clients to access various services, APIs, or microservices within a system or an organization. It's an essential component in modern software architectures and serves several purposes:

- **Aggregation and Composition**: API Gateways can aggregate multiple APIs or microservices into a unified API, simplifying the client experience by providing a single interface to access various functionalities.
- **Routing and Load Balancing**: They handle incoming requests from clients and route them to the appropriate backend services. Load balancing ensures that requests are distributed efficiently across multiple instances of these services.
- **Security and Authentication**: API Gateways often enforce security protocols such as authentication, authorization, and encryption. They authenticate incoming requests, verify user identity, and enforce access control policies.
- **Request Transformation**: They can modify or transform requests and responses to match the requirements of different backend services or to ensure compatibility with various client devices.
- **Caching and Rate Limiting**: API Gateways can cache responses from backend services to improve performance and also enforce rate limits to prevent abuse or excessive usage of services.
- **Monitoring and Analytics**: They provide insights into API usage, performance metrics, and error tracking, enabling better monitoring and analysis of API traffic.
- **Versioning and Lifecycle Management**: They facilitate versioning of APIs, allowing the introduction of new features or changes without disrupting existing clients. They also help in managing the lifecycle of APIs, including deprecation or retirement.

API Gateways play a crucial role in decoupling clients from the underlying microservices architecture, providing a layer of abstraction that simplifies the interaction between clients and the backend services. They streamline API management, enhance security, improve performance, and enable better control and governance over the APIs exposed by an organization.


## 1.2 Apache Kafka
Apache Kafka is an open-source distributed event streaming platform designed for handling real-time data feeds and processing. It was originally developed by LinkedIn and later open-sourced as a part of the Apache Software Foundation.

Key Concepts in Kafka:
- Topics: Kafka organizes data into topics, which serve as feeds or categories where data is published. Producers write messages to topics, and consumers read from these topics.
- Partitions: Topics are divided into partitions, which are individual, ordered, and immutable sequences of messages. Partitions allow data to be distributed across multiple Kafka brokers for scalability and parallel processing.
- Brokers: Kafka runs as a cluster of servers called brokers. Brokers are responsible for storing and managing the partitions, handling message storage and retrieval, and managing replication and fault tolerance.
- Producers: Applications or systems that publish data to Kafka topics are known as producers. They write messages to Kafka topics.
- Consumers: Applications or systems that subscribe to topics and process the published data are known as consumers. They read messages from Kafka topics and process them.
- Consumer Groups: Consumers are organized into groups, and Kafka assigns partitions to different consumers within a group for load balancing and parallel processing. Each partition is consumed by only one consumer within a group, ensuring that multiple consumers work together to process a topic.

Key Features:
- Scalability: Kafka is horizontally scalable, allowing it to handle large volumes of data by distributing it across multiple brokers and partitions.
- Fault Tolerance: Kafka replicates partitions across multiple brokers to ensure fault tolerance. If a broker fails, partitions can still be accessed from replicas.
- Durability: Messages written to Kafka are persisted, allowing data to be stored and replayed as needed. This durability ensures data integrity.
- High Throughput: Kafka is optimized for high-throughput and low-latency data transmission, making it suitable for real-time data streaming and processing.

Use Cases:
- Real-time Data Processing: Used for real-time analytics, monitoring, and processing of large streams of data.
- Log Aggregation: Collects logs from different sources for centralized storage and analysis.
- Messaging Systems: Acts as a high-throughput message queue for communication between different parts of a system.
- Stream Processing: Facilitates continuous processing of data streams for various applications such as fraud detection, IoT, and more.

Apache Kafka's architecture and capabilities make it a popular choice for building scalable, fault-tolerant, and real-time data streaming applications in various industries.

- Pros:
  - **Zero copy**: data read does not rely on the OS. That said, the data can be transfered directly from the disk, to the kernel, to the NIC Buffer (Network Interface Controller) and sent to the costumer. A no-zero copy system would pass the data to the application layer (userland) first, and then go down all the way again to the Socket Buffer, NIC, and then transfer it to the consumer. Depending on the hardware, it can even use Direct memory access (DMA). DMA is a feature of computer systems that allows certain hardware subsystems to access main system memory independently of the central processing unit (CPU). 


  ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fff3743a9-915c-44c8-9bc3-562a754035f8_2469x2973.jpeg)
  - **Sequential I/O**: Sequential I/O in Kafka works as follows:

    Writing: Producers write messages to Kafka topics. These messages are appended to the end of the appropriate partition within the topic. Kafka ensures that messages from a single producer within a partition are strictly ordered based on their offsets.

    Reading: Consumers can read messages from Kafka topics. They can choose to read from a specific partition or across partitions within a topic. Consumers maintain an offset to keep track of the last message they have consumed. By specifying this offset, they can read messages sequentially, starting from that point.

    Kafka's ability to handle sequential I/O efficiently is crucial for maintaining the order of messages and providing fault tolerance, scalability, and high throughput in handling streams of data.


# Optimizations
- Caching: with Redis (it uses RAM memory).
- Connection Pool for databases: waaay faster than creating new connections
- Avoid the n + 1 query problem: The chief symptom of this problem is that there are many, many queries being performed. Typically, this happens when you structure your code so that you first do a query to get a list of records, then subsequently do another query for each of those records. The more queries you perform, the more time it takes to get the results back, with each trip to the database server taking time and resources. In contrast, a single query, even if it's complex, can be optimized by the database server and only requires one trip to the database, which will usually be much faster than many small queries.
- Pagination: is a technique used in software design and user interfaces to manage and display large sets of data in smaller, manageable portions or pages. It's particularly useful when presenting data to users, especially in web applications or when dealing with databases that contain extensive records. Pagination is commonly implemented using techniques like SQL's LIMIT and OFFSET clauses for database queries, or in web interfaces through frontend frameworks that support paginated data loading and display.
- Lightweight Serialization: Lightweight serialization refers to the process of serializing data in a more efficient, compact, and often faster manner compared to traditional serialization methods. The term "lightweight" implies that the serialization process is optimized for reduced overhead, decreased data size, and improved performance, particularly in resource-constrained environments or high-throughput systems. Examples are MessagePack and protobuf.
- Compression: Compression is a technique used in computer science and data transmission to reduce the size of files or data streams. The process involves encoding information in a more compact form, resulting in smaller file sizes or reduced data sizes for transmission. Compression offers benefits such as faster data transmission, reduced storage requirements, and improved network performance.


# 3. Interview

## 3.1 Framework

1. **Introduction** (5 minutes)
2. **Understand the Problem and estabilish design scope** (5 minutes):
   - Questions will be open-ended and vague. Focus on what's important and ask as many questions as necessary to understand problem fully.
   - **User cases (description of sequences of events that, taken together, lead to a system doing something useful)**
     - It's a red flag jump right to the solution
     - Who is going to use it? **How** are they going to use it?
     - Focus on the top few features to build. Make sure the interviewer agrees with the feature list.
   - **Constraints (Non-functional requirements)**:
     - Ask questions about non-functional requirements. Focus on scale and performance, but others are security, consistency, freshness and accuracy.
     - Mainly identify traffic and data handling constraints at scale.
     - Calculate (using math) estimates to understand the idea of scale
     - Scale of the system such as requests per second, requests types, data written per second, data read per second
     - Special system requirements such as multi-threading, read or write oriented.
   - At the end, you will have a feature list and a few non-functional requirements to satisfy.

3. **Propose high-level design and validate the requirements with the interviewer** (20 minutes)
    - **API Design:**
       - The most common approach, is starting with a top down approach, designing the APIs. The APIs will be the ones that will sign a contract with the backend systems and the users (clients). 
       - It should be clear, after obtaining the requirements list, which APIs will be needed. Make sure you use industry standard to define the APIs and make sure it's satisfying the system requirements.
       - Do not introduce APIs that are not in the requirements list.
       - Make sure whether to use REST, GraphQL, WebSockets and etc...
    - **High-level design diagram**:
      - For many designs, it's common to start with a Load Balancer or a API Gateway. 
      - Behind that, it will be located the services we defined with the interviewer in the features list. 
      - Behind that, we define the data storage layer, where the data will be persisted (databases). It's usually not important to decide which database option (MySQL, MongoDB, Redis, Scylla, ElasticSearch...) to use in this stage. This should be done in the Deep Dive section, and only after the data schema is designed.
      - While developing the high level design, mantain a list of disccusion points for later. Resist the temptation to detail much of the system and dive deep before the full picture of the high-level design.
    - **Data model and schema**:
      - Discuss data access patterns, read/write ratio and QPS (Queries per second). Discuss and choose the right database and indexing options based on this metrics.
      - Make judgement calls: if the data model (sharding...) is the key part of the non-functional requirements, discuss this in the deep dive section.
    - Review the design. Make sure everything from the requirements list is present.
4. **Design deep dive** (15 minutes)
   - Discuss with the interviewer what should be dive deep. This section is where the non-functional requirements will be discussed and proposed. The higher the level of the role, more important this section is.
   - Identify areas that could be problematic and discuss solutions and trade-offs.
5. **Wrap up** (5 minutes)
   - Summarize the solution.
6. **Q&A** (5 minutes)

## 3.2 Tips:
- The more senior the role, the more important it is to demonstrate skills on handling and suggesting the non-functional requirements.
- Pick up the clues from body language of the interviewer to check if the solution is satisfying or not. Ask if the interviewer has any questions or concerns.