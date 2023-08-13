from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import os
import os
os.environ["http_proxy"] = "http://127.0.0.1:1080"
os.environ["https_proxy"] = "http://127.0.0.1:1080"
os.environ["OPENAI_API_KEY"] = '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'
template="请扮演律师的角色,对咨询人应保持耐心、专业、负责的态度，认真斟酌后答复其问题，并与咨询人进行沟通，向其提问，获取案件基本情况和信息。"\
          "按要求完成下面的10个类别的信息收集任务，按照以下顺序按点收集，一定要将以下提到的信息全部收集完整，最后将收集的信息整理成表格，一次只能提问一个问题:"\
          "1. 咨询者及受伤职工基本信息：咨询人的身份信息、咨询人与受伤职工的关系信息或与受伤职工用人单位的关系信息、受伤职工的身份信息（是否属于外地来沪从业人员）、受伤职工用人单位的信息（是否属于建筑施工、矿山企业）、受伤职工与用人单位的关系信息（是否属于灵活就业等特殊用工）。"\
          "2. 工伤事件细节：受伤职工的工作岗位、职责、伤害发生的时间、地点、具体过程及与工作的关系、单位的考勤方式。若涉及到第三人侵权的，需关注第三人侵权责任的认定。"\
          # "3. 劳动合同情况：受伤职工与用人单位之间是否签订劳动合同。签订劳动合同的，需对劳动合同签订主体、合同履行地、合同期限、工资、岗位等信息予以关注；未签订劳动合同的，需了解用人单位与所有员工是否均未签订劳动合同、是否有证明受伤职工与用人单位之间存在劳动关系的证据。"\
          # "4. 薪资及保险情况：受伤职工的工作岗位、工资标准、工资发放方式。用人单位缴纳工伤保险费的情况，包括有无缴纳工伤保险费、工伤保险的类型以及缴费标准。"\
          # "5. 救治和医疗情况：受伤人员的送医过程以及救治情况，包括具体护理人员情况、有无跨地区治疗、支付的医药费数额，付款记录及票据是否保留，治疗费用是否系用人单位支付等。 "\
          # "6. 休养与薪资发放情况：受伤职工发生工伤后停工休养时长，有无请病假，假条是否提供给用人单位，用人单位有无准许。 受伤职工停工留薪期间工资发放情况，包括有无发放、发放方式以及发放的具体数额。"\
          # "7. 离职情况：受伤职工离职情况，包括是否离职、离职时间、离职手续的办理、离职时用人单位是否给予补偿、补偿的名目、补偿的具体数额、双方是否签订协议等。"\
          # "8. 工伤和劳动能力鉴定：受伤职工的工伤认定、劳动能力鉴定情况，包括工伤待遇是否已经申报、申报主体、申报结果、鉴定结果以及是否已经收到相应工伤待遇款项、收到款项的数额、时间等。"\
          # "9. 职业病情况：如果职工患职业病，律师需询问病情及诊断、鉴定情况。"\
          # "10. 其他相关信息:与工伤案件有关的其他具体信息。"

system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template="{input}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    MessagesPlaceholder(variable_name="history"),
    human_message_prompt
])
llm = ChatOpenAI(temperature=0.5)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

while True:
    output = conversation.predict(input=input())
    print(output)


