"""
=======================================================================================================
    Marvellous SmartHire AI Agent
=======================================================================================================
Author  : Lahuraj Namdev Wadkar
Date    : 13/11/2026

Descriptiion    :
This project is a text-based AI Mock Interview Agent.

This project demonstrates the  practical implementation of:

1. AI Agent
2. LLM Integration
3. Prompt Engineering
4. Answer Evalution
5. Intervie Automation
6. Report Generation
7. Memory through interview history
========================================================================================================
"""

from questions import questions
from interview_agent import MockInterviewAgent
from report_generator import save_report

def print_header():
    """
    Function Name: print_header
    """

    print("="*100)
    print("     AI Mock Interview Agent")
    print("     Text Based Version")
    print("     Author : Lahuraj NAmdev Wadkar")
    print("     Date : 13/11/2026")
    print("="*100)

def show_menu():
    """
    Function Name : show_menu
    Description : Display interview mode options to the user.
    """

    print("\nSelect Interview Mode:")
    print("1. Start Full Interview")
    print("2. Start Topic-wise Interview")
    print("3. Exit")

def get_available_topics():
    """
    Function Name : get_available_topics
    Description : Extracts unique topics from question bank.
    Return Value : List of available topics
    """

    topics = []

    #Traverse all questions and collect unique topics
    for item in questions:
        if item["topic"] not in topics:
            topics.append(item["topic"])

    return topics

def start_interview(agent, selected_questions):
    """
    Function Name : start_interview
    Description   : Conducts the interview by asking selected questions.
    Parameters    :
        agent          :Object of MockInterviewAgnet class
        selected_questions: List of questions selected for interview 
    """

    #Ask questions one by one
    for index, item in enumerate(selected_questions, start=1):
        topic = item["topic"]
        question = item["question"]

        print("\n" + "="*100)
        print(f"Questions {index}")
        print("Topic :", topic)
        print("Question :", question)
        print("="*100)

        #Accept students answer through text input
        answer = input("\nEnter your answer:\n")

        #Handle empty answer case
        if answer.strip() == "":
            answer = "Student did not provide any answer."

        print("\nEvaluating your answer using LLM...")
        print("Please wait while AI interviwe Agent is analyzing your response.")

        #Send questions and answer to AI Agent for evaluation
        evaluation = agent.evaluate_answer(topic, question, answer)
        print("\nEvaluation Result :")
        print("-"*100)
        print(evaluation)
        print("-"*100)

        #Ask user whether to continue interview or stop
        choice = input("\nDo you want to continue? yes/no:")
        if choice.lower() != "yes":
            break

def main():
    """
    Function Name : main
    Description   : Entry point of the AI interview Agent project.
    """

    print_header()

    print("\nWelcome to SmartHire AI Mock Interview Agent.")
    print("This system conducts technical interviews using text input and LLM evaluation")
    print("This project is designed for practical understanding of AI Agents.\n")

    #Accept Student Name.
    student_name = input("Enter student name:")

    #If student name is empty. Use default name
    if student_name.strip() == "":
        student_name = "Student"

    #Create object of MockInterview Agnet
    agent = MockInterviewAgent(student_name)

    print(f"Welcome {student_name} to AI Mock Interview.")
    print("The interview will evaluate  your technical answers using LLM.")

    while True:
        show_menu()

        choice = input("\nEnter your choice : ")

        #Full interview mode
        if choice == "1":
            start_interview(agent, questions)

            # Generate final report after interview completion
            report = agent.generate_final_report()
            print(report)

            #Save final report into report folder
            filename = save_report(student_name, report)

            print("\nInterview completed successfully.")
            print("Final report generated successfully.")
            print("Report saved at :", filename)

            break

        #Topic wise interview mode
        elif choice == "2":
            topics = get_available_topics()

            print("\nAvailable topics :")

            #Display available topics
            for index, topic in enumerate(topics, start=1):
                print(f"{index}. {topic}")

                try:
                    topic_choice = int(input("\nSelect topic number: "))
                    #validate topic choice
                    if topic_choice < 1 or topic_choice > len(topics):
                        print("\nInvalid topic number. Please try again.")
                        continue
                    selected_topic = topics[topic_choice -1]

                    selected_questions = []

                    #Select questions matching selected topic
                    for item in questions:
                        if item["topic"] == selected_topic:
                            selected_questions.append(item)

                    print(f"\nYour selected topic : {selected_topic}")

                    start_interview(agent, selected_questions)

                    #Generate final report
                    report = agent.generate_final_report()
                    print(report)

                    #Save final report into report folder
                    filename = save_report(student_name, report)
                    print("\nInterview completed successfully.")
                    print("Final report generated successfully.")
                    print("Report saved at :", filename)
                    break
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")

        #Exit option
        elif choice == "3":
            print("\nThank you for using AI Mock Interview Agent.")
            print("Keep learning. keep practicing.")
            break
        #Invalid menu option
        else:
            print("\n Invalid choice. Please try again.")

#Program execution start from here

if __name__ == "__main__":
    main()
