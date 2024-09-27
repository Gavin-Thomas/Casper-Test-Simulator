import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import random
import time
import os
import subprocess
import sys

# List of scenarios. Each scenario is a dictionary with 'scenario' and 'questions' keys.
scenarios = [
    {
        "scenario": "As a software engineer at a tech company, you discover that a new feature being developed may inadvertently collect users' personal data without their explicit consent. This data could be used to improve the service, but it also raises privacy concerns. You bring this up to your project manager, but they dismiss your concerns, emphasizing the importance of meeting the project deadline.",
        "questions": [
            "What are the ethical implications of proceeding with the feature as it is?",
            "How would you address your concerns with your manager or higher-ups?",
            "What steps can you take to ensure user privacy is respected while meeting project goals?"
        ]
    },
    {
        "scenario": "You are a member of a community volunteer group that is planning a charity event. During a meeting, one of the members proposes an idea that could potentially raise a lot of money but might also exploit vulnerable individuals. Some members are excited about the idea, while others are hesitant.",
        "questions": [
            "How would you navigate the differing opinions within the group?",
            "What factors should be considered when deciding whether to proceed with the idea?",
            "How can you contribute to finding a solution that aligns with the group's values?"
        ]
    },
    {
        "scenario": "In your workplace, you notice that a coworker is being excluded from important meetings and social events due to their cultural background. This exclusion is affecting their performance and morale. The management seems unaware of the issue.",
        "questions": [
            "What steps would you take to address the situation?",
            "How can you support your coworker without overstepping boundaries?",
            "Why is inclusivity important in a team environment?"
        ]
    },
    {
        "scenario": "As a teacher, you find that one of your students is consistently submitting work that appears to be completed by someone else. Confronting the student might strain your relationship, but ignoring the issue could undermine academic integrity.",
        "questions": [
            "How would you approach the student about your concerns?",
            "What are the potential consequences of ignoring the situation?",
            "How can you help the student get back on track academically?"
        ]
    },
    {
        "scenario": "You're part of a project team, and one member is taking credit for work they didn't do, including some of your contributions. This behavior is affecting team morale and the fairness of performance evaluations.",
        "questions": [
            "How should you address the issue of credit-taking with your colleague?",
            "What role does transparency play in team projects?",
            "How can you prevent this situation from happening in the future?"
        ]
    },
    {
        "scenario": "While working at a financial institution, you discover that a senior employee is manipulating accounts to meet targets, which could be illegal and harm clients. Reporting them could risk your job and reputation.",
        "questions": [
            "What ethical dilemmas does this situation present?",
            "Should you report the senior employee? Why or why not?",
            "What are the potential consequences of both action and inaction?"
        ]
    },
    {
        "scenario": "You are leading a project, and a key team member is struggling with their tasks due to personal issues. The project deadline is approaching, and their performance is putting the project at risk.",
        "questions": [
            "How would you address the team member's performance issues?",
            "What support can you offer while ensuring project success?",
            "Why is it important to balance empathy and accountability?"
        ]
    },
    {
        "scenario": "At a family gathering, a relative makes an offensive joke that targets a marginalized group. Other family members either laugh uncomfortably or stay silent. You're unsure whether to speak up or let it pass to keep the peace.",
        "questions": [
            "How should you respond to the offensive joke?",
            "What are the potential impacts of addressing or not addressing the comment?",
            "How can you promote a more respectful environment in social settings?"
        ]
    },
    {
        "scenario": "You are a journalist assigned to cover a story that could expose corruption in a major corporation. However, publishing the story might lead to legal repercussions and affect your publication's relationship with advertisers.",
        "questions": [
            "What ethical considerations should guide your decision to publish or not?",
            "How do you balance the public's right to know with potential risks?",
            "What steps can you take to ensure responsible journalism?"
        ]
    },
    {
        "scenario": "As a manager, you notice that one of your employees is frequently making errors that could compromise safety. They have been with the company for a long time and are well-liked, but their mistakes are becoming more frequent.",
        "questions": [
            "How would you address the safety concerns with the employee?",
            "What factors should you consider when deciding on possible actions?",
            "Why is safety a non-negotiable aspect in the workplace?"
        ]
    },
    {
        "scenario": "You are a member of a sports team, and your coach is pushing the team to use aggressive tactics that border on violating the rules. Some teammates are uncomfortable but fear speaking up might reduce their playing time.",
        "questions": [
            "What are the ethical implications of following the coach's strategy?",
            "How can you and your teammates address your concerns with the coach?",
            "Why is sportsmanship important in competitive environments?"
        ]
    },
    {
        "scenario": "In a collaborative academic project, you discover that another student has plagiarized their portion of the work. The project is due soon, and their actions could affect everyone's grades.",
        "questions": [
            "How should you handle the situation with your teammate?",
            "What are the potential consequences of submitting the plagiarized work?",
            "How can academic integrity be maintained in group projects?"
        ]
    },
    {
        "scenario": "While volunteering at a local shelter, you notice that donations are not being distributed properly, and some staff members might be taking items for personal use.",
        "questions": [
            "What steps should you take upon noticing this issue?",
            "How can you ensure that the shelter's resources are used appropriately?",
            "Why is accountability important in non-profit organizations?"
        ]
    },
    {
        "scenario": "You are attending a professional conference, and you overhear two attendees discussing confidential information about their company's upcoming merger. This information could impact the stock market.",
        "questions": [
            "What should you do with the information you've overheard?",
            "What are the ethical considerations in this scenario?",
            "How might sharing this information affect various stakeholders?"
        ]
    },
    {
        "scenario": "As an employee, you are asked to work on a project that conflicts with your personal values. Refusing the project might affect your career advancement, but participating makes you uncomfortable.",
        "questions": [
            "How should you approach your manager about your concerns?",
            "What factors should you consider when deciding whether to participate?",
            "Why is it important to align professional work with personal ethics?"
        ]
    },
    {
        "scenario": "As a senior software engineer at a leading tech firm specializing in artificial intelligence, you are heading a team tasked with developing an advanced facial recognition system for use in international airports. During the testing phase, you uncover that the algorithm has a significantly higher error rate when identifying individuals from certain ethnic minorities, leading to false positives that could result in unwarranted detentions or interrogations. Concerned about the potential for racial profiling and civil rights violations, you bring this issue to your project manager. However, the manager emphasizes that the company has a lucrative contract with a government agency that is insistent on rolling out the system before an upcoming global summit. He suggests that while the concerns are valid, they can be addressed in future updates and that delaying the project could have severe financial and reputational repercussions for the company.",
        "questions": [
            "What are the ethical implications of deploying the facial recognition system despite known flaws affecting specific ethnic groups?",
            "How should you handle the situation when your manager is prioritizing deadlines and contracts over ethical concerns?",
            "What steps can you take to advocate for a fair and unbiased technology before it is implemented in real-world scenarios?"
        ]
    },
    {
        "scenario": "You are a city council member in a rapidly growing metropolitan area. A proposal has been submitted to build a new commercial complex that promises significant economic benefits, including job creation and increased tax revenue. However, the proposed site for the complex is currently a community park that serves as one of the few green spaces in a densely populated, low-income neighborhood. The park is a vital gathering place for community events and is frequented by families and children. While the development would boost the city's economy, it would also deprive an already underserved community of essential recreational space. During a public hearing, residents express strong opposition to the project, voicing concerns about environmental impact and loss of community identity. The developers counter with promises of new jobs and potential funding for alternative community projects.",
        "questions": [
            "How should you weigh the economic benefits against the community's needs and environmental concerns?",
            "What factors should influence your decision-making process in this situation?",
            "How can you work towards a solution that supports economic development while preserving community assets?"
        ]
    },
    {
        "scenario": "As a senior researcher at a pharmaceutical company, you are part of a team developing a new medication that has shown great promise in treating a rare but deadly disease. During the final phase of clinical trials, a small percentage of participants begin to exhibit severe side effects, some of which are life-threatening. The company stands to gain substantial profits upon the drug's approval, and there is pressure from upper management to minimize the reporting of these adverse effects to expedite the approval process. They argue that the benefits outweigh the risks and that disclosing all side effects could lead to unnecessary delays or denial from regulatory agencies. You are aware that withholding this information could put future patients at risk but also recognize that the drug could save many lives if brought to market quickly.",
        "questions": [
            "What are the ethical considerations involved in reporting or not reporting the severe side effects?",
            "How should you address the pressure from management while upholding ethical research practices?",
            "What responsibilities do you have towards patients, regulatory bodies, and the broader medical community?"
        ]
    },
    {
        "scenario": "You are an investigative journalist who has received anonymous documents revealing that a major corporation has been illegally dumping toxic waste into a local river for years. Publishing this story could lead to significant environmental cleanup and hold the corporation accountable. However, the corporation is a major employer in the area, and exposing them could result in massive layoffs, harming the local economy. Additionally, the corporation has a history of aggressive legal action against whistleblowers and media outlets, which could lead to a protracted legal battle for your publication. Your editor is hesitant to run the story without concrete evidence that can withstand legal scrutiny, and there is pressure to consider the potential fallout on the community.",
        "questions": [
            "What ethical dilemmas do you face in deciding whether to publish the story?",
            "How can you balance the public's right to know with the potential negative consequences for the community?",
            "What steps can you take to ensure responsible journalism while uncovering the truth?"
        ]
    },
    {
        "scenario": "Working as a high school teacher in an underfunded district, you notice that one of your brightest students, who has aspirations to attend a prestigious university, is frequently absent and falling behind. Upon speaking with the student, you learn that they have taken on a part-time job to support their family financially, as their parents have recently lost employment. The school has strict attendance policies, and the administration is unsympathetic to personal circumstances, threatening suspension if absences continue. The student is torn between their educational goals and their family's immediate needs.",
        "questions": [
            "How can you support the student in balancing their educational aspirations with their family obligations?",
            "What steps can you take within the school's policies to advocate for the student?",
            "Why is it important to consider individual student circumstances in educational settings?"
        ]
    },
    {
        "scenario": "As a financial advisor at a well-respected investment firm, you discover that a colleague has been manipulating client portfolios to generate higher commissions for themselves, resulting in significant financial losses for some clients. Reporting this misconduct could lead to a major scandal, loss of client trust, and substantial financial penalties for the firm. Your supervisor, upon being informed, suggests handling the matter internally to avoid public exposure and advises you to remain silent while they 'manage' the situation. You are aware that clients continue to be at risk, and regulatory bodies would expect such misconduct to be reported immediately.",
        "questions": [
            "What are the ethical and legal obligations you have in this situation?",
            "How should you respond to your supervisor's suggestion to keep the matter internal?",
            "What are the potential consequences of both reporting and not reporting the misconduct?"
        ]
    },
    {
        "scenario": "Serving on the board of a non-profit organization dedicated to providing clean water in developing countries, you discover that the organization has been overstating the number of wells built and communities served in its annual reports to attract more donations. This misrepresentation has helped secure substantial funding but has not been used as effectively as donors believe. Bringing this issue to light could damage the organization's reputation and result in a loss of funding, potentially halting ongoing projects. Other board members argue that the 'ends justify the means' and that the overall mission is too important to risk negative publicity.",
        "questions": [
            "What ethical issues arise from the organization's misrepresentation of its accomplishments?",
            "How should you address the situation with fellow board members who believe in the current approach?",
            "Why is transparency important in maintaining donor trust and organizational integrity?"
        ]
    },
    {
        "scenario": "As a medical professional in a hospital's emergency department, you are treating a patient who was involved in a violent altercation and is a suspected gang member. During treatment, the patient confides in you about plans for retaliatory violence against a rival group, which could endanger multiple lives. Patient confidentiality laws restrict you from disclosing information shared during treatment. However, failing to act on this information could result in harm to others. Law enforcement is present in the hospital due to the nature of the incident and is eager for any information that could prevent further violence.",
        "questions": [
            "How do you navigate the conflict between patient confidentiality and public safety?",
            "What steps can you take to address the potential threat without violating ethical guidelines?",
            "Why is patient confidentiality a critical aspect of medical ethics, even in challenging situations?"
        ]
    },
    {
        "scenario": "You are a mid-level manager in a corporation that is implementing a new software system company-wide. During the rollout, you discover that the software has significant security vulnerabilities that could expose sensitive employee and customer data to cyberattacks. The IT department is aware of the issues but is downplaying the risks to meet the launch schedule. When you bring up your concerns to upper management, they dismiss them, citing the cost and time required to address the vulnerabilities. They insist on proceeding, emphasizing the competitive advantage the new system provides.",
        "questions": [
            "What are the potential risks of proceeding with the software launch despite known security issues?",
            "How should you advocate for addressing the vulnerabilities before full implementation?",
            "What responsibilities do companies have in protecting data, and why is it important to prioritize security?"
        ]
    },
    {
        "scenario": "While working as a human resources director, you become aware that the company's recruitment process is biased, favoring candidates from certain universities and backgrounds, which results in a lack of diversity in the workplace. Attempts to introduce diversity and inclusion initiatives have been met with resistance from senior management, who believe that the current approach ensures high-quality hires. Employees from underrepresented groups have expressed feelings of isolation and limited opportunities for advancement. The company's public image is that of an inclusive and progressive employer.",
        "questions": [
            "What ethical considerations arise from the company's recruitment and promotion practices?",
            "How can you effectively promote diversity and inclusion in the face of management resistance?",
            "Why is workplace diversity important for both employees and the organization as a whole?"
        ]
    },
        {
        "scenario": "Describe a time when you had to make a difficult decision that affected others. What was the situation, and how did you handle it?",
        "questions": [
            "What factors did you consider when making your decision?",
            "How did your decision impact those involved?",
            "What did you learn from this experience about leadership and responsibility?"
        ]
    },
    {
        "scenario": "Tell me about an experience where you failed at something. How did you respond to the failure, and what did you learn?",
        "questions": [
            "What were the circumstances leading to the failure?",
            "How did you cope with the disappointment?",
            "In what ways has this failure contributed to your personal or professional growth?"
        ]
    },
    {
        "scenario": "Reflect on a situation where you had to work as part of a team to achieve a common goal. What was your role, and how did you contribute to the team's success?",
        "questions": [
            "What challenges did the team face, and how were they overcome?",
            "How did you facilitate collaboration among team members?",
            "What did this experience teach you about teamwork?"
        ]
    },
    {
        "scenario": "Consider the ethical implications of genetic engineering in humans.",
        "questions": [
            "What are the potential benefits and risks of genetic engineering?",
            "How should society regulate the use of genetic technologies?",
            "What ethical principles should guide decisions in this field?"
        ]
    },
    {
        "scenario": "Describe a time when you had to give constructive feedback to someone. How did you approach the situation?",
        "questions": [
            "What was the feedback, and why was it necessary?",
            "How did the person receive your feedback?",
            "What strategies did you use to ensure the feedback was effective?"
        ]
    },
    {
        "scenario": "Tell me about a time when you had to adapt to a significant change. How did you manage the transition?",
        "questions": [
            "What was the change, and why was it significant?",
            "What steps did you take to adjust?",
            "How has this experience influenced your ability to handle future changes?"
        ]
    },
    {
        "scenario": "Reflect on an ethical dilemma you have faced. How did you resolve it?",
        "questions": [
            "What were the conflicting values or principles involved?",
            "What process did you follow to make your decision?",
            "What did you learn about yourself through this experience?"
        ]
    },
    {
        "scenario": "Consider the role of social media in modern society.",
        "questions": [
            "What are the positive and negative impacts of social media?",
            "How does social media influence public opinion and behavior?",
            "What responsibilities do users and platforms have to promote healthy online interactions?"
        ]
    },
    {
        "scenario": "Describe a situation where you had to manage your time effectively to meet multiple deadlines.",
        "questions": [
            "What strategies did you use to prioritize your tasks?",
            "How did you handle any stress or pressure?",
            "What did you learn about time management from this experience?"
        ]
    },
    {
        "scenario": "Tell me about a time when you helped resolve a conflict between others.",
        "questions": [
            "What was the nature of the conflict?",
            "How did you intervene to help resolve it?",
            "What were the outcomes, and what did you learn about conflict resolution?"
        ]
    },
    {
        "scenario": "Reflect on the importance of cultural competence in today's globalized world.",
        "questions": [
            "Why is understanding different cultures important?",
            "How can individuals develop cultural competence?",
            "What impact does cultural competence have on personal and professional relationships?"
        ]
    },
    {
        "scenario": "Describe an instance when you took initiative to improve a process or situation.",
        "questions": [
            "What motivated you to take action?",
            "What steps did you take to implement the improvement?",
            "What was the result, and how was it received by others?"
        ]
    },
    {
        "scenario": "Consider the ethical considerations of data privacy in the digital age.",
        "questions": [
            "What are the challenges associated with protecting personal data?",
            "How should companies balance data collection with user privacy?",
            "What role do individuals have in safeguarding their own information?"
        ]
    },
    {
        "scenario": "Tell me about a time when you had to learn something new in a short period. How did you approach the learning process?",
        "questions": [
            "What was the new skill or knowledge you needed to acquire?",
            "What strategies did you use to learn effectively?",
            "How did this experience influence your approach to learning?"
        ]
    },
    {
        "scenario": "Reflect on the role of empathy in effective communication.",
        "questions": [
            "How does empathy enhance interpersonal interactions?",
            "Can you provide an example where empathy improved a conversation?",
            "What techniques can be used to develop greater empathy?"
        ]
    },
    {
        "scenario": "Describe a situation where you set a challenging goal for yourself. What steps did you take to achieve it?",
        "questions": [
            "What made the goal challenging?",
            "How did you stay motivated throughout the process?",
            "What did you learn from striving toward this goal?"
        ]
    },
    {
        "scenario": "Consider the impact of climate change on future generations.",
        "questions": [
            "What are the most pressing environmental issues we face today?",
            "How can individuals and communities contribute to solutions?",
            "What ethical responsibilities do we have toward future generations?"
        ]
    },
    {
        "scenario": "Tell me about a time when you received criticism. How did you handle it?",
        "questions": [
            "What was the nature of the criticism?",
            "How did you respond emotionally and practically?",
            "What changes, if any, did you make as a result?"
        ]
    },
    {
        "scenario": "Reflect on the importance of resilience in overcoming adversity.",
        "questions": [
            "What does resilience mean to you?",
            "Can you share an example where resilience helped you succeed?",
            "How can one develop and strengthen their resilience?"
        ]
    },
    {
        "scenario": "Describe an experience where you had to consider someone else's perspective to resolve a problem.",
        "questions": [
            "What was the situation, and why was their perspective different?",
            "How did understanding their viewpoint help in finding a solution?",
            "What did this teach you about empathy and problem-solving?"
        ]
    },
    {
        "scenario": "Consider the ethical responsibilities of professionals in sharing accurate information.",
        "questions": [
            "Why is honesty important in professional communications?",
            "What are the potential consequences of spreading misinformation?",
            "How can professionals ensure they are providing reliable information?"
        ]
    },
    {
        "scenario": "Tell me about a time when you had to make a quick decision under pressure.",
        "questions": [
            "What was the situation, and why was quick decision-making necessary?",
            "How did you arrive at your decision?",
            "What was the outcome, and what did you learn from the experience?"
        ]
    },
    {
        "scenario": "Reflect on the role of ethics in leadership.",
        "questions": [
            "Why are ethical principles important for leaders?",
            "Can you provide an example of ethical leadership?",
            "How can leaders promote ethical behavior within their teams?"
        ]
    },
    {
        "scenario": "Describe a time when you had to persuade others to see your point of view.",
        "questions": [
            "What was the context, and who were you trying to persuade?",
            "What arguments or strategies did you use?",
            "What was the result, and what did you learn about persuasion?"
        ]
    },
    {
        "scenario": "Consider the importance of mental health awareness in society.",
        "questions": [
            "Why is it important to address mental health issues openly?",
            "What barriers prevent people from seeking help?",
            "How can communities promote mental well-being among their members?"
        ]
    },
    {
    "scenario": "You are a senior researcher at a pharmaceutical company developing a new drug. During the final stages of clinical trials, you discover that the drug has unforeseen severe side effects that were not previously reported. Reporting these findings could lead to the halt of the drug's approval process, resulting in significant financial losses for the company and delaying access to a potentially life-saving medication for patients. However, not reporting the side effects could endanger lives and undermine the company's ethical responsibilities.",
    "questions": [
        "What ethical responsibilities do you have in deciding whether to report the drug's severe side effects?",
        "How can you balance the company's financial interests with patient safety and well-being?",
        "What steps can you take to ensure transparency and accountability in the drug approval process?"
        ]
    },
    {
        "scenario": "As a data analyst for a large retail chain, you uncover patterns that suggest a competitor is using unethical data scraping techniques to gather sensitive customer information. Reporting this could lead to legal action against the competitor, but it might also strain your relationship with other industry partners and result in retaliation. Additionally, your company might be tempted to leverage this information for its own competitive advantage, raising further ethical concerns.",
        "questions": [
            "What ethical considerations should guide your decision to report the competitor's unethical data practices?",
            "How can you protect customer privacy while addressing the unethical behavior you've discovered?",
            "What are the potential risks and benefits for your company and the industry if the unethical practices are reported or ignored?"
        ]
    },
    {
        "scenario": "You are a project leader in a software development company tasked with creating an AI-driven recruitment tool. During development, you realize that the AI model is inadvertently introducing bias against candidates from certain demographic backgrounds. Reporting the bias could delay the product launch and require significant revisions, but ignoring it could perpetuate discrimination and harm the company's reputation for promoting diversity and inclusion.",
        "questions": [
            "What ethical obligations do you have in addressing the AI model's bias in the recruitment tool?",
            "How can you mitigate the bias in the AI model while maintaining project timelines?",
            "What are the potential consequences for the company and job candidates if the bias is not addressed?"
        ]
    },
    {
        "scenario": "As an environmental consultant for a construction company, you assess a new development project and discover that the proposed site is a critical habitat for an endangered species. Proceeding with the project would lead to the destruction of the habitat, threatening the species' survival. Reporting this finding could result in project delays, increased costs, and potential loss of contracts, while ignoring it would mean contributing to environmental harm and violating conservation ethics.",
        "questions": [
            "What ethical considerations are involved in deciding whether to report the environmental impact of the development project?",
            "How can you advocate for sustainable practices within the construction company?",
            "What are the long-term implications for the environment and the company's reputation if the habitat destruction is not addressed?"
        ]
    },
    {
        "scenario": "You are a software engineer at a social media company. You discover that the platform's algorithm promotes content that increases user engagement but also spreads misinformation and polarizing content. Reporting the issue could lead to a redesign of the algorithm, potentially reducing user engagement and profits, but not reporting it would allow harmful content to proliferate, undermining the platform's responsibility to provide accurate and balanced information.",
        "questions": [
            "What ethical responsibilities do you have in addressing the algorithm's promotion of harmful content?",
            "How can you balance the company's profit motives with the need to prevent misinformation and polarization?",
            "What steps can be taken to ensure the platform fosters a healthy and informed user community?"
        ]
    },
    {
        "scenario": "As a human resources manager in a global corporation, you become aware that a subsidiary in a developing country is violating labor laws by imposing excessive working hours and inadequate safety measures. Reporting these violations could result in legal action, fines, and strained relationships with local partners, but ignoring them would mean condoning unethical labor practices and potentially exploiting workers.",
        "questions": [
            "What ethical obligations do you have in addressing the labor violations at the subsidiary?",
            "How can you work towards improving labor conditions while maintaining the corporation's global operations?",
            "What are the potential consequences for workers and the company's reputation if the violations are not addressed?"
        ]
    },
    {
        "scenario": "You are a financial advisor at a wealth management firm and learn that a senior colleague is steering clients towards investments that offer higher commissions for the firm but are not in the clients' best interests. Reporting this unethical behavior could lead to internal conflict, potential retaliation, and harm to your career, but ignoring it would mean compromising your integrity and failing to protect clients' financial well-being.",
        "questions": [
            "What ethical principles should guide your decision to report the colleague's behavior?",
            "How can you advocate for clients' best interests while navigating workplace dynamics?",
            "What are the potential impacts on clients and the firm if the unethical behavior is not addressed?"
        ]
    },
    {
        "scenario": "As a university administrator, you discover that the admissions office has been favoring applicants from certain elite backgrounds, neglecting merit-based criteria and diversity goals. Reporting this bias could lead to institutional scrutiny, legal challenges, and a reevaluation of the admissions process, but ignoring it would perpetuate inequality and undermine the university's commitment to diversity and fairness.",
        "questions": [
            "What ethical considerations are involved in addressing bias within the admissions process?",
            "How can you promote equitable admissions practices while maintaining the university's reputation?",
            "What steps can be taken to ensure that the admissions process is fair and inclusive for all applicants?"
        ]
    },
    {
        "scenario": "You are a product manager at a tech company developing a smart home device. During testing, you discover that the device collects more user data than necessary and transmits it to third parties without explicit consent. Reporting this privacy issue could delay the product launch and require redesigning data collection practices, but ignoring it would mean compromising user privacy and potentially violating data protection laws.",
        "questions": [
            "What ethical responsibilities do you have in addressing the device's data collection practices?",
            "How can you ensure user privacy while advancing the product's development?",
            "What are the potential consequences for users and the company if the privacy issues are not resolved?"
        ]
    },
    {
        "scenario": "As a consultant for a public health organization, you find evidence that a proposed health initiative could inadvertently exclude marginalized communities, exacerbating health disparities. Reporting this oversight could lead to a reevaluation and redesign of the initiative, delaying its implementation, but not reporting it would mean the initiative fails to serve all communities effectively and perpetuates inequality.",
        "questions": [
            "What ethical obligations do you have in ensuring the health initiative is inclusive?",
            "How can you advocate for equitable health outcomes within the organization?",
            "What are the potential impacts on marginalized communities and public health if the initiative is not made inclusive?"
        ]
    },
    {
        "scenario": "You are a cybersecurity specialist for a financial institution, and you discover that the company's security measures are inadequate, making it vulnerable to data breaches. Reporting this could lead to significant investments in security infrastructure, impacting the company's profitability, but ignoring it would risk exposing sensitive customer information and damaging the institution's reputation.",
        "questions": [
            "What ethical responsibilities do you have in addressing the company's cybersecurity vulnerabilities?",
            "How can you persuade the company to invest in necessary security measures while balancing financial constraints?",
            "What are the potential consequences for customers and the institution if the vulnerabilities are not addressed?"
        ]
    },
    {
        "scenario": "As a data privacy officer at a healthcare organization, you learn that patient data is being used for research purposes without proper consent, violating privacy regulations. Reporting this malpractice could lead to legal repercussions, loss of trust, and financial penalties for the organization, but ignoring it would mean continuing to misuse sensitive patient information and breaching ethical standards.",
        "questions": [
            "What ethical obligations do you have in addressing the misuse of patient data?",
            "How can you ensure compliance with privacy regulations while supporting valuable research?",
            "What are the potential impacts on patients and the organization if the data misuse is not corrected?"
        ]
    },
    {
        "scenario": "You are a journalist at a major news outlet and receive a tip about government corruption that could lead to significant public interest reporting. However, verifying the information would require extensive resources, and publishing without solid evidence could result in defamation lawsuits. Additionally, the source is anonymous, raising concerns about the credibility of the information.",
        "questions": [
            "What ethical principles should guide your decision to investigate and potentially publish the corruption story?",
            "How can you balance the public's right to know with the need for accurate and verified reporting?",
            "What steps can you take to protect yourself and your news outlet while pursuing the story?"
        ]
    },
    {
        "scenario": "As a manager in a tech startup, you discover that the company is using deceptive marketing tactics to exaggerate the capabilities of its new software product. Reporting this could result in reputational damage, loss of sales, and financial repercussions, but not reporting it would mean continuing unethical practices that mislead customers and competitors.",
        "questions": [
            "What ethical considerations are involved in deciding whether to report the company's deceptive marketing tactics?",
            "How can you address the issue to promote honest communication with customers?",
            "What are the potential consequences for the company and its stakeholders if the deceptive practices are not corrected?"
        ]
    },
    {
        "scenario": "You are a teacher at a private school and realize that the institution is systematically excluding students from lower socioeconomic backgrounds through biased admissions practices and inadequate financial aid. Reporting this could lead to a review of the admissions policies, potential funding cuts, and changes in the school's demographic makeup, but ignoring it would mean perpetuating inequality and denying opportunities to deserving students.",
        "questions": [
            "What ethical obligations do you have in addressing the school's exclusionary practices?",
            "How can you advocate for more inclusive admissions policies while maintaining the school's standards?",
            "What are the potential impacts on students and the school's reputation if the issues are not addressed?"
        ]
    },
    {
        "scenario": "As a quality assurance manager in a food manufacturing company, you discover that certain products have been contaminated due to a flaw in the production process. Reporting the contamination could lead to product recalls, financial losses, and damage to the company's reputation, but not reporting it would risk consumer health and safety, potentially leading to serious health consequences.",
        "questions": [
            "What ethical responsibilities do you have in addressing the contaminated products?",
            "How can you manage the situation to protect consumers while minimizing negative impacts on the company?",
            "What steps can be taken to prevent similar issues from occurring in the future?"
        ]
    },
    {
        "scenario": "You are a financial analyst at a hedge fund and notice that your firm's investment strategies are indirectly supporting companies with poor environmental records, contributing to environmental degradation. Reporting this could lead to a reevaluation of investment policies and potential loss of high-return investments, but ignoring it would mean perpetuating harmful environmental practices and compromising your personal ethical standards.",
        "questions": [
            "What ethical considerations should guide your decision to report the firm's investment strategies?",
            "How can you advocate for environmentally responsible investments within the hedge fund?",
            "What are the potential consequences for the environment and the firm's reputation if the issue is not addressed?"
        ]
    },
    {
        "scenario": "As a designer at a fashion brand, you discover that the company is using fabrics sourced from suppliers that engage in unethical labor practices, including child labor and unsafe working conditions. Reporting this could lead to supply chain disruptions, increased costs, and reputational damage, but not reporting it would mean supporting unethical practices and contributing to human rights abuses.",
        "questions": [
            "What ethical obligations do you have in addressing the use of unethical fabrics in your company's products?",
            "How can you work with the company to ensure ethical sourcing while maintaining product quality and cost-effectiveness?",
            "What are the potential impacts on workers and the company's brand if the issue is not addressed?"
        ]
    }
]

selected_scenarios = random.sample(scenarios, 14)

# --------------------------------------------------------------------------------------------

class CasperTestSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Casper Test Simulator")
        self.master.geometry("800x600")

        self.current_scenario_index = 0
        self.time_left = 0
        self.timer_id = None
        self.all_answers = []
        self.video_responses = []

        self.ffmpeg_process = None

        # Device indices
        self.video_device_index = None
        self.audio_device_index = None

        # Keep track of breaks taken
        self.breaks_taken = set()

        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()
        instructions = tk.Label(self.master, text="Before starting, please set up your video and audio devices.", font=('Helvetica', 14))
        instructions.pack(pady=10)
        device_button = tk.Button(self.master, text="Set Up Devices", command=self.setup_devices, font=('Helvetica', 16))
        device_button.pack(pady=20)
        start_button = tk.Button(self.master, text="Start Test", command=self.start_test, font=('Helvetica', 16))
        start_button.pack(pady=20)

    def setup_devices(self):
        # List available devices
        devices_info = self.list_avfoundation_devices()
        if not devices_info:
            messagebox.showerror("Error", "Could not retrieve device list.")
            return

        # Display devices to the user in a scrollable window and then prompt for indices
        self.show_device_list_window(devices_info)

    def list_avfoundation_devices(self):
        try:
            list_cmd = ['ffmpeg', '-f', 'avfoundation', '-list_devices', 'true', '-i', '']
            result = subprocess.run(list_cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            devices_info = result.stderr

            # Parse devices_info to extract only the device list
            device_list = self.parse_device_list(devices_info)
            return device_list
        except Exception as e:
            return None

    def parse_device_list(self, devices_info):
        # Extract lines containing device information
        lines = devices_info.split('\n')
        device_lines = []
        capture = False
        for line in lines:
            if 'AVFoundation video devices' in line or 'AVFoundation audio devices' in line:
                capture = True
                device_lines.append(line)
            elif capture:
                if line.startswith('[') and 'AVFoundation' not in line:
                    capture = False
                else:
                    device_lines.append(line)
        return '\n'.join(device_lines)

    def show_device_list_window(self, devices_info):
        # Create a new top-level window
        device_window = tk.Toplevel(self.master)
        device_window.title("Available Devices")
        device_window.geometry("600x400")

        # Create a scrollable text widget
        text_widget = scrolledtext.ScrolledText(device_window, wrap=tk.WORD, font=('Helvetica', 12))
        text_widget.pack(expand=True, fill='both', padx=10, pady=10)

        # Insert the devices info into the text widget
        text_widget.insert(tk.END, devices_info)
        text_widget.config(state=tk.DISABLED)

        # Add a button to close the window and prompt for device indices
        ok_button = tk.Button(device_window, text="OK", command=lambda: [device_window.destroy(), self.prompt_for_device_indices()], font=('Helvetica', 12))
        ok_button.pack(pady=10)

    def prompt_for_device_indices(self):
        # Ask for device indices
        self.video_device_index = simpledialog.askstring("Video Device Index", "Enter the video device index (e.g., 0):")
        self.audio_device_index = simpledialog.askstring("Audio Device Index", "Enter the audio device index (e.g., 0):")

        if self.video_device_index is None or self.audio_device_index is None:
            messagebox.showwarning("Warning", "Device indices not set. Recording may not work properly.")

    def start_test(self):
        if self.video_device_index is None or self.audio_device_index is None:
            messagebox.showwarning("Warning", "Device indices not set. Please set up your devices before starting.")
            return
        self.all_answers = []
        self.current_scenario_index = 0  # Reset the scenario index
        self.breaks_taken = set()  # Reset the breaks taken
        self.next_scenario()

    def next_scenario(self):
        if self.current_scenario_index >= len(selected_scenarios):
            self.show_results()
            return

        # Check if it's time for a 5-minute break
        if self.current_scenario_index in [6, 10] and self.current_scenario_index not in self.breaks_taken:
            # Time for a 5-minute break
            self.breaks_taken.add(self.current_scenario_index)
            self.time_left = 300  # 5 minutes
            self.show_break_screen()
        else:
            # Determine if current scenario is a video or written response
            if self.current_scenario_index < 6:
                self.show_scenario_video()
            else:
                self.show_scenario_written()

    # ------------------ Written Response Methods ------------------

    def show_scenario_written(self):
        self.clear_screen()
        self.current_scenario = selected_scenarios[self.current_scenario_index]
        scenario_text = self.current_scenario['scenario']

        scenario_label = tk.Label(self.master, text=f"Scenario {self.current_scenario_index + 1}", font=('Helvetica', 16, 'bold'))
        scenario_label.pack(pady=10)

        scenario_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=('Helvetica', 14))
        scenario_display.insert(tk.END, scenario_text)
        scenario_display.config(state=tk.DISABLED)
        scenario_display.pack(expand=True, fill='both', padx=20, pady=10)

        self.next_button = tk.Button(self.master, text="Next", command=self.show_questions_written, font=('Helvetica', 14))
        self.next_button.pack(side='right', padx=20, pady=10)

        self.time_left = 60  # 1 minute for scenario
        self.update_timer_label()
        self.start_timer(self.show_questions_written)

    def show_questions_written(self):
        self.stop_timer()
        self.clear_screen()
        questions = self.current_scenario['questions']
        self.answers = []
        self.answer_entries = []

        frame = tk.Frame(self.master)
        frame.pack(expand=True, fill='both', padx=20, pady=10)

        for idx, question in enumerate(questions):
            question_label = tk.Label(frame, text=f"Question {idx+1}: {question}", font=('Helvetica', 14))
            question_label.pack(anchor='w', pady=(10, 0))

            answer_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=5, font=('Helvetica', 12))
            answer_text.pack(fill='both', pady=(0, 10))
            self.answer_entries.append(answer_text)

        self.next_button = tk.Button(self.master, text="Next", command=self.save_answers_written, font=('Helvetica', 14))
        self.next_button.pack(side='right', padx=20, pady=10)

        self.time_left = 300  # 5 minutes for questions
        self.update_timer_label()
        self.start_timer(self.end_question_period_written)

    def save_answers_written(self):
        self.stop_timer()
        answers = [entry.get("1.0", tk.END).strip() for entry in self.answer_entries]
        self.all_answers.append({
            'scenario': self.current_scenario['scenario'],
            'questions': self.current_scenario['questions'],
            'answers': answers
        })
        self.current_scenario_index += 1
        self.next_scenario()

    def end_question_period_written(self):
        self.next_button.config(state=tk.DISABLED)
        self.save_answers_written()

    # ------------------ Video Response Methods ------------------

    def show_scenario_video(self):
        self.clear_screen()
        self.current_scenario = selected_scenarios[self.current_scenario_index]
        scenario_text = self.current_scenario['scenario']
        questions = self.current_scenario['questions']

        scenario_label = tk.Label(self.master, text=f"Scenario {self.current_scenario_index + 1}", font=('Helvetica', 16, 'bold'))
        scenario_label.pack(pady=10)

        scenario_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, height=8, font=('Helvetica', 14))
        scenario_display.insert(tk.END, scenario_text)
        scenario_display.config(state=tk.DISABLED)
        scenario_display.pack(fill='both', padx=20, pady=10)

        for idx, question in enumerate(questions):
            question_label = tk.Label(self.master, text=f"Question {idx+1}: {question}", font=('Helvetica', 12))
            question_label.pack(anchor='w', padx=20)

        self.next_button = tk.Button(self.master, text="Next", command=self.start_video_response, font=('Helvetica', 14))
        self.next_button.pack(side='right', padx=20, pady=10)

        self.time_left = 60  # 1 minute to read scenario and questions
        self.update_timer_label()
        self.start_timer(self.start_video_response)

    def start_video_response(self):
        self.stop_timer()
        self.clear_screen()

        self.recording_label = tk.Label(self.master, text="Recording in progress...", font=('Helvetica', 16), fg='red')
        self.recording_label.pack(pady=20)

        self.time_left = 60  # 1 minute video response
        self.update_timer_label()

        self.video_filename = f"video_response_{self.current_scenario_index + 1}.mp4"
        self.video_responses.append(self.video_filename)

        self.next_button = tk.Button(self.master, text="Next", command=self.end_video_recording, font=('Helvetica', 14))
        self.next_button.pack(side='right', padx=20, pady=10)

        # Start the video recording
        self.record_video()

        # Start the timer countdown
        self.start_timer(self.end_video_recording)

    def record_video(self):
        if self.video_device_index is None or self.audio_device_index is None:
            messagebox.showerror("Error", "Video or audio device indices are not set.")
            self.end_video_recording()
            return

        device_str = f"{self.video_device_index}:{self.audio_device_index}"

        self.video_filename = f"video_response_{self.current_scenario_index + 1}.mp4"  # Ensure .mp4 extension

        cmd = [
            'ffmpeg',
            '-y',  # Overwrite output file if it exists
            '-f', 'avfoundation',
            '-framerate', '30',
            '-video_size', '1280x720',
            '-i', device_str,  # Video and audio devices
            '-t', '60',  # Duration in seconds
            '-vcodec', 'libx264',  # Use H.264 video codec
            '-acodec', 'aac',      # Use AAC audio codec
            '-pix_fmt', 'yuv420p',  # Set pixel format
            self.video_filename
        ]

        try:
            # Start ffmpeg process
            self.ffmpeg_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            # Check if ffmpeg process exits immediately
            self.master.after(500, self.check_ffmpeg_process)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start video recording: {e}")
            self.end_video_recording()

    def check_ffmpeg_process(self):
        if self.ffmpeg_process.poll() is not None:
            # Process has exited
            stderr_output, _ = self.ffmpeg_process.communicate()
            messagebox.showerror("ffmpeg Error", f"ffmpeg exited with error:\n{stderr_output}")
            self.end_video_recording()
        else:
            # Process is still running, no action needed
            pass

    def end_video_recording(self):
        self.stop_timer()
        # Stop the ffmpeg process
        if self.ffmpeg_process and self.ffmpeg_process.poll() is None:
            self.ffmpeg_process.terminate()
            self.ffmpeg_process.wait()
        self.recording_label.destroy()
        self.next_button.destroy()
        self.timer_label.destroy()
        # Save scenario and questions for review
        self.all_answers.append({
            'scenario': self.current_scenario['scenario'],
            'questions': self.current_scenario['questions'],
            'video': self.video_filename
        })
        self.current_scenario_index += 1
        self.next_scenario()

    # ------------------ Common Methods ------------------

    def show_break_screen(self):
        self.clear_screen()
        break_label = tk.Label(self.master, text="Break Time! Next scenario will start soon.", font=('Helvetica', 16))
        break_label.pack(expand=True)

        self.next_button = tk.Button(self.master, text="Next", command=self.end_break, font=('Helvetica', 14))
        self.next_button.pack(side='right', padx=20, pady=10)

        self.update_timer_label()
        self.start_timer(self.next_scenario)

    def end_break(self):
        self.stop_timer()
        self.next_scenario()

    def show_results(self):
        self.clear_screen()
        results_label = tk.Label(self.master, text="Test Completed! Here are your responses:", font=('Helvetica', 16))
        results_label.pack(pady=10)

        results_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=('Helvetica', 12))
        results_display.pack(expand=True, fill='both', padx=20, pady=10)

        for idx, entry in enumerate(self.all_answers):
            results_display.insert(tk.END, f"Scenario {idx+1}:\n{entry['scenario']}\n\n")
            if 'answers' in entry:
                for q_idx, question in enumerate(entry['questions']):
                    results_display.insert(tk.END, f"Question {q_idx+1}: {question}\n")
                    results_display.insert(tk.END, f"Your Answer:\n{entry['answers'][q_idx]}\n\n")
            elif 'video' in entry:
                for q_idx, question in enumerate(entry['questions']):
                    results_display.insert(tk.END, f"Question {q_idx+1}: {question}\n")
                # Create a closure to capture the current filename
                def play_video_closure(filename=entry['video']):
                    return lambda: self.play_video(filename)
                video_button = tk.Button(results_display, text=f"Play Video Response {idx+1}", command=play_video_closure())
                results_display.window_create(tk.END, window=video_button)
                results_display.insert(tk.END, "\n\n")
            results_display.insert(tk.END, "-"*80 + "\n")

        results_display.config(state=tk.DISABLED)

    def play_video(self, filename):
        # Open the video file with the default media player
        if sys.platform.startswith('darwin'):
            # macOS
            subprocess.call(['open', filename])
        else:
            messagebox.showerror("Error", "This program currently supports video playback only on macOS.")

    def start_timer(self, callback):
        self.stop_timer()
        self.countdown(self.time_left, callback)

    def countdown(self, remaining_time, callback):
        if remaining_time <= 0:
            self.timer_label.config(text="Time Left: 00:00")
            self.master.after(0, callback)
        else:
            mins, secs = divmod(remaining_time, 60)
            time_str = f"Time Left: {mins:02d}:{secs:02d}"
            self.timer_label.config(text=time_str)
            self.timer_id = self.master.after(1000, self.countdown, remaining_time - 1, callback)

    def stop_timer(self):
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
            self.timer_id = None

    def update_timer_label(self):
        if hasattr(self, 'timer_label'):
            self.timer_label.destroy()
        self.timer_label = tk.Label(self.master, text="", font=('Helvetica', 12))
        self.timer_label.place(relx=1.0, rely=0.0, anchor='ne')

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def on_closing(self):
        # Clean up resources when closing the application
        self.stop_timer()
        if self.ffmpeg_process and self.ffmpeg_process.poll() is None:
            self.ffmpeg_process.terminate()
            self.ffmpeg_process.wait()
        self.master.destroy()

def main():
    root = tk.Tk()
    app = CasperTestSimulator(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()

