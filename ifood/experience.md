# iFood

## Values
- Empreendedorismo: Temos um sonho grande e agimos como donos(as). Nossa alma é empreendedora e queremos ir sempre além. Para nós, o céu não é o limite.
- Resultados: Somos pessoas obcecadas por resultados e sempre buscamos alta performance. Reconhecemos nosso time com base na entrega, sem vieses.
- Inovação: Acreditamos no poder da inovação por um futuro mais próspero. Por isso, temos sede de disrupção, tecnologia e IA. Testamos, erramos e mudamos de forma simples e rápida.
- All together: Juntos e juntas, com colaboração, equidade e diversidade de pessoas, somos melhores! Nessa jornada, que parece impossível, celebramos as conquistas e encaramos tudo com leveza e bom humor.

## Interview

- STAR Method:
  - Situation: Open with a brief description of the Situation and context of the story (who, what, where, when, how).
  - Task: Explain the Task you had to complete highlighting any specific challenges or constraint (e.g., deadlines, costs, other issues).
  - Action: Describe the specific Actions that you took to complete the task. These should highlight desirable traits without needing to state them (i.e., initiative, intelligence, dedication, leadership, understanding, etc.)
  - Result: Close with the result of your efforts. Include figures or metrics to quantify the result if possible. Provide measurable specifics where you can, and be prepared to back them up.

### Techinical Questions

- Cite padrões de resiliência: Fault Tolerance (Redundancy, graceful degradation, and failover mechanisms), Recovery (Backup and restore procedures, automated recovery processes, and effective incident response.), Redundancy (Having multiple servers, data centers, or cloud regions to ensure continuous service availability), Monitoring and Observability (Logging, monitoring, and distributed tracing to detect and diagnose problems in real-time.), Automation (Automated deployment, scaling, and self-healing mechanisms), Scalability (Horizontal scaling, load balancing, and elastic cloud infrastructure).
  
  
- Diga o que é uma row lock, lock tables; a "row-lock" refers to a mechanism used to control access to a specific row of data within a database table during transactions. It is a part of the concurrency control mechanisms implemented to ensure data consistency and prevent conflicts between concurrent transactions. The LOCK TABLES statement is used to control access to one or more tables in a database, explicitly acquiring locks. This can be useful in scenarios where a series of operations need to be performed atomically, and you want to ensure that other transactions do not interfere.
- Como escalar um microsserviço no k8s:
  1. `kubectx <namespace>`
  2. `kubectl get deployments`
  3. `kubectl scale deployment <deployment-name> --replicas=<desired-replica-count>`
  - **Autoscaling**: Kubernetes also provides Horizontal Pod Autoscaling (HPA) for automatic scaling based on observed - CPU utilization or custom metrics. You can create an HPA resource for your microservices.
  - **Load Balancing**: Ensure that your microservices are behind a service with a LoadBalancer or Ingress to distribute traffic across the replicated instances.
  - **Readiness and Liveness Probes**: Configure readiness and liveness probes in your microservices' PodSpec to ensure proper scaling behavior.

- 5 principios do solid, sobre orientação a objetos: design principles encourage us to create more maintainable, understandable, and flexible software.
  1. **Single Responsibility**: a class should only have one responsibility. Furthermore, it should only have one reason to change.
    - Testing – A class with one responsibility will have far fewer test cases.
    - Lower coupling – Less functionality in a single class will have fewer dependencies.
    - Organization – Smaller, well-organized classes are easier to search than monolithic ones.

  2. **Open/Closed (Open for Extension/Closed for Modification):** classes should be open for extension but closed for modification. In doing so, we stop ourselves from modifying existing code and causing potential new bugs in an otherwise happy application.
  3. **Liskov Substitution**: In simpler terms, if a class is a subtype (derived class) of another class (base class), instances of the derived class should be able to replace instances of the base class without affecting the correctness of the program. This principle promotes the idea that derived classes should extend the behavior of the base class without changing its expected functionality.
  4. **Interface Segregation**: larger interfaces should be split into smaller ones. By doing so, we can ensure that implementing classes only need to be concerned about the methods that are of interest to them.
  5. **Dependency Inversion**: The principle of dependency inversion refers to the decoupling of software modules. This way, instead of high-level modules depending on low-level modules, both will depend on abstractions. High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions
  
- Qual design pattern que você mais usa? Singleton, 
- Projeto que se orgulhou?
- Projeto que não se orgulhou? MVP at Hoobox
- O que acha de trabalhar em um ambiente diverso?:
- Voce tem experiência com AWS?
- What kind of instrumentation do you apply to ensure high-performance architecture design?



### Stories

- **When did you f*ck up production? And how did you solve it.**: #transparency #humble #autonomy
  - **Nugget**: I'll tell you a time where I made a problematic deployment because I did not make a plan for it.
  - **Situation**: One of my first tasks was to work on order complements flow in iFood. An order complement is a new delivery request for an item that was not delivered or when the order is too big to one delivery man.
  - **Task**: My task was to improve this feature code. The flow was implemented using AWS Lambda, AWS SQS and Node.js. The task involved changing an environment variable using Terraform.
  - **Action**: I've improved the flow as described and tested the changes on the validation environment. The deployment process had 2 steps (because of the deployment window): updating the environment variable and deploying the new lambda code. This service did not have canary releases. My plan was to deliver the first part before lunch and the second in the afternoon.
  - **Result**: The lambda code did not know how to work with the new environment variable label and that made the complement order flow to stop working. Even though this flow was not critical,  it increased the contact rate from the restaurants. This could be avoided if I planned the deployment better and performed a risk analysis.


- **Tell me about a time when you had a conflict with a co-worker:**
  - Two cases: Griaule and RISC-6
  - **RISC-6**:
    - **Nugget**: disagreement of the scope of the project to be delivered in a short time.
    - **Task**: This last semester I did a project along with other 5 students to design and implement a 32-bit RISC-V system (with CPU, memory and peripherals), and deploy it in a FPGA chip within 5 months. Regarding the memory, a commercial CPU requires unnaligned reads and writes, but this requires a weeks of designing a state machine to proper handle this. My colleague Daniel was responsible on designing and implementing the memory and he was too hyped up to develop a lot of features in the memory, not taking in consideration seriously the time it would take.
    - **Action**: we talked about the importance of incremental but consistant and working deliveries. We could also develop the extra features, but the core should be developed fully first so that we would have a consistant working system
    - **Result**: After a healthy conversation of really undestanding the weights and time that each task would take, he agreed on developing the core first and even thanked me later for making he see how important is to plan and schedule tasks.
  
  - **Griaule**: Code Style Disagreement: #Ownership #HaveBackboneDisagreeAndCommit
    - **Nugget**: I'll tell you a time where I had a disagreement with a teammate involving changes and I could convince him it was a good thing for the team.
    - **Situation**: Griaule was in the process of remaking its legacy applications that were desktop, to the web. In the past, having a good UI and UX was not a priority ever, but when remaking these apps, quality of the products were a priority. I was responsible for building these applications on the frontend using React and other JavaScript technologies. They were not in much contact with other software companies and its engineers were mainly CS students or old timers, so they did not have much knowledge on how to improve the quality of their products and they were finding out how to do.
    - **Task**: I've suggested we could use static style checking to ensure quality and improve maintenance time to our new projects, seeing that our project was being built without ensuring these things. As I said, this was not in practice by the engineering team I was involved with, even being successful in convincing my manager,   it would take a time to convince that was a good thing.
    - **Action**: The team I was working with were young, and despite the fact that they were too used to developing in a fast way, they liked to know how to improve and be a better frontend engineer. So my approach was telling my experience with static style checking and how I improved and started coding better after this.
    We decided as a team that static style checking would be a step to validate before an increment on code was done, and one developer did not like this after. He complained how fixing these errors and even errors that were done by somebody else took so much time (even though he being a good code reviewer). We talked and I told the importance of preventing these errors and ensuring quality in our work, just the way we did in code reviews. I sat down with him and I helped him fix those errors. 
    - **Result**: The whole team saw improvement on how they were coding and reading other teammates projects and started adding this pipeline to other projects that we were developing.

- **What was the most difficult bug that you fixed in the past 6 months?**:
  - **Nugget:** I'll tell about the time I had trouble on optmizing a low level operation on cryptography algorithm. After fixing it, I learned how important is to proper undestand the environment of each problem and do not assume standards of other environments to be true in others.
  - **Situation**:  The most difficult bug I fixed recently was actually a low-level problem. My bachelor's thesis is on optmizing the NIST selected standard algorithm for lightweight cryptography, Ascon, for the `riscv64` architecture.
  - **Task**:  On the decryption algorithm, after processing the ciphertext, there's a final operation to update the internal state (it uses the sponge construction). I made an hypothesis of optmizing this operation using shifts instead of loading data.
  - **Action**: On my way to optimize this doing shift operations instead of loading data, it wouldn't decrypt it right. I investigate the issue for hours, reading the algorithm specification over and over, just to realize the problem was that I was handling with the reverse endianess. 
  - **Result**: After that, I reversed the endianess and I've managed to do a proper optimization on the algorithm. I realized how important is to doubt any standards, since that the more you dive low, less standards are defined. Also, standards do not automatically translate to different scopes.

- **Time management has become a necessary factor in productivity. Give an example of a time-management skill you've learned and applied at work.**
  - **Nugget**: Time management and project planning on the tasks to be developed during the internship period at Meta.
  - **Situation**: when I joined Meta, I received a plan of the tasks that should be developed over the internship. The job involved develop UI features and cross-app integrations to increase product adoption, as well experiment features with users.  
  - **Task**: All of these tasks had to be developed within 3 months, and the manager would have a weekly meeting with me to check it out how I was performing and developing the product features to check if I would be a good fit for the company. I also wanted to enjoy the most of that professional experience in such a large scale company.
  - **Action**: For each task, I analyzed the current challenge, what was done before and talked to designers and other engineers in case I needed help better understanding the issue. 
  - **Result**: I learned to plan each task within due time and the best solution for the right time. As well learning to understand more of the source code on my own and collaborate whenever need was needed it. This experience was essential to build self-confidence and lead projects with responsability, quality and efficiency even when I'm not the smartest engineer in the room.

- **How do you tackle challenges? Name a difficult challenge you faced while working on a project, how you overcame it, and what you learned.**
  1. Study the context: Without the proper context you can miss important details of the the challenge.
  2. Get the full storyline of the challenge: From the birth to what was done in the past to fix it.
  3. Hypothesis time: create possible hypothesis and rank which have greater possibilitiies.
  4. Solution time: After selecting the proper hypothesis, select the one that have the highest score on both solving the issue for the right time.
  5. Analysis: did it solve the problem?
  6. Future: analyze other hypothesis and discard them if they were not true, and decide if a better solution should be planned to be proper implemented.

- **Where do you see yourself in five years?**: My true passion is both solving challenges using computers within collaboration but also doing that together, inspiring young ones to challenge themselves to solving real world problems. In 5 years from now I see myself as Staff Engineer or even director of technology, solving large scale problems together with othe experts from whom I can learn more, building the next-gen architectures for large impact services and helping the company's tech talent grow by helping new engineers but also in hiring new ones.

- **How do you stay up to date with the latest technologies?**: HackerNews, X and GitHub. I'm very curious and I dive deep even on topics that are not my expertise to properly understand how thing works, after all, it's just all computing. Later, I've been studying machine learning engineering, reading source code and playing with neural nets engines, as well keeping updated on new LLMs and AI architectures.

- **What aspects of your work are most often criticized?**
  - Self-validation;
  - Be more engaged and study strategy, since I have good calls on these tpes of meetings, but actually enjoy that much.
  - Lead projects with confidence. 
  - Overthinking;
- **Tell me about a time you met a tight deadline.**: RISC-6/Meta Coworking features/Hoobox MVP


## Questions to Make
- How collaboration is being done?
- Do engineers still interact with plataform and SREs? Can they contribute in RFCs?