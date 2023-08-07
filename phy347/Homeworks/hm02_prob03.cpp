#include "stdafx.h"
#include <iostream> 
#include <string> 
#include <fstream>
#include <iomanip>
#include <cmath> 

using namespace std; 

struct StudentData
{
    int studentID; 
    string first_name; 
    string last_name; 
    int exam1; 
    int exam2; 
    int exam3; 
    int total; 
    char ch; 
}; 

const int SIZE = 9; 
const int INFO = 4; 

// Function prototypes
void openInputFile(ifstream &, string); 
void getTotal(StudentData[]); 
void getGrade(StudentData[]); 
void calcLowest(StudentData[], int &, int &, int &, int &, int[]);  
void calcHighest(StudentData[], int &, int &, int &, int &, int[]);  
void getAverage(StudentData[], int, double &, double &, double &, double &, double[]); 
void getStd(StudentData[], double &, double &, double &, double &, double &, double &, double &, double &, double[]); 
void print(StudentData[], int[], int[], double[], double[]); 
void sort(StudentData[]); 

int main()
{
    // Variables 
    StudentData arr[SIZE]; 
    int lowest1, lowest2, lowest3, lowest4; // Stores lowest exam scores
    int highest1, highest2, highest3, highest4; // Holds highest exam scores
    double average1 = 0, average2 = 0, average3 = 0, average4 = 0; // Represents average of each exam 
    double std1 = 0, std2 = 0, std3 = 0, std4 = 0; // Holds standard deviation for Exams 1-3 and Total 
    int lowest[INFO] = {};
    int highest[INFO] = {}; 
    double average[INFO] = {}; 
    double standardDeviation[INFO] = {}; 

    ifstream inFile; 
    string inFileName = "scores.txt"; 

    // Call function to read data in file
    openInputFile(inFile, inFileName);

    // Read data into an array of structs 
    for(int count = 0; count < SIZE; count++)
    {
        inFile >> arr[count].studentID >> arr[count].first_name >> arr[count].last_name >> arr[count].exam1 >> arr[count].exam2 >> arr[count].exam3; 
    }

    // Close input file
    inFile.close();  

    // Get score total for each student 
    getTotal(arr); 

    // Determine grade for each student
    getGrade(arr); 

    // Calculate lowest scores in each exam and total scores
    calcLowest(arr, lowest1, lowest2, lowest3, lowest4, lowest); 

    // Calculate highest scores in each exam and total scores  
    calcHighest(arr, highest1, highest2, highest3, highest4, highest); 

    // Calculate average of each exam and the average of the total scores
    getAverage(arr, SIZE, average1, average2, average3, average4, average); 

    // Calculate standard deviation of each category 
    getStd(arr, std1, std2, std3, std4, average1, average2, average3, average4, standardDeviation); 

    cout << "\n"; 

    // Print unsorted data
    print(arr, lowest, highest, average, standardDeviation); 

    cout << "\n"; 

    // Sort data 
    sort(arr); 

    // Print sorted data
    print(arr, lowest, highest, average, standardDeviation); 

    system("PAUSE"); 

    return 0; 
}

void openInputFile(ifstream &inFile, string inFileName)
{
    //Open the file
    inFile.open(inFileName);

    //Input validation
    if (!inFile)
    {
        cout << "Error to open file." << endl;
        cout << endl;
        return;
    }
}

void getTotal(StudentData arr[])
{
    for(int i = 0; i < SIZE; i++)
    {
        arr[i].total = arr[i].exam1 + arr[i].exam2 + arr[i].exam3; 
    }
}

void getGrade(StudentData arr[])
{
    for(int i = 0; i < SIZE; i++)
    {
        if(arr[i].total >= 270)
            arr[i].ch = 'A'; 
        else if(arr[i].total >= 240)
            arr[i].ch = 'B'; 
        else if(arr[i].total >= 210)
            arr[i].ch = 'C'; 
        else if(arr[i].total >= 180)
            arr[i].ch = 'D'; 
        else 
            arr[i].ch = 'F'; 
    }
}

/**
* Pre-condition: 
* Post-condition: 
*/
void calcLowest(StudentData arr[], int &lowest1, int &lowest2, int &lowest3, int &lowest4, int lowest[])
{
    int smallest = 0; 

    lowest1 = arr[0].exam1; 
    lowest2 = arr[0].exam2; 
    lowest3 = arr[0].exam3; 
    lowest4 = arr[0].total; 

    // Loop to determine lowest score from Exam1, 2, 3, and Total
    for (int i = 0; i < SIZE; i++)
    {
        if (lowest1 > arr[i].exam1)
        {
            lowest1 = arr[i].exam1; 
            smallest = i; 
        }

        if (lowest2 > arr[i].exam2)
        {
            lowest2 = arr[i].exam2; 
            smallest = i; 
        }

        if (lowest3 > arr[i].exam3)
        {
            lowest3 = arr[i].exam3; 
            smallest = i; 
        }

        if (lowest4 > arr[i].total)
        {
            lowest4 = arr[i].total; 
            smallest = i; 
        }
    }

    // Loop lowest values into an array of size 4 
    for(int index = 0; index < INFO; index++)
    {
        if(index == 0)
            lowest[0] = lowest1; 
        else if(index == 1)
            lowest[1] = lowest2; 
        else if(index == 2)
            lowest[2] = lowest3; 
        else if(index == 3)
            lowest[3] = lowest4; 
        else 
            cout << "Fail!" << endl; 
    }
}

void calcHighest(StudentData arr[], int &highest1, int &highest2, int &highest3, int &highest4, int highest[])
{
    int biggest = 0; 

    highest1 = arr[0].exam1; 
    highest2 = arr[0].exam2; 
    highest3 = arr[0].exam3; 
    highest4 = arr[0].total; 

    // Loop to determine highest score from Exam1, 2, 3, and Total 
    for (int i = 0; i < SIZE; i++)
    {
        if (highest1 < arr[i].exam1)
        {
            highest1 = arr[i].exam1; 
            biggest = i; 
        }

        if (highest2 < arr[i].exam2)
        {
            highest2 = arr[i].exam2; 
            biggest = i; 
        }

        if (highest3 < arr[i].exam3)
        {
            highest3 = arr[i].exam3; 
            biggest = i; 
        }

        if (highest4 < arr[i].total)
        {
            highest4 = arr[i].total; 
            biggest = i; 
        }
    }

    // Loop highest values into an array of size 4 
    for(int index = 0; index < INFO; index++)
    {
        if(index == 0)
            highest[0] = highest1; 
        else if(index == 1)
            highest[1] = highest2; 
        else if(index == 2)
            highest[2] = highest3; 
        else if(index == 3)
            highest[3] = highest4; 
        else 
            cout << "Fail!" << endl; 
    }
}

void getAverage(StudentData arr[], int size, double &average1, double &average2, double &average3, double &average4, double average[])
{
    int sum1 = 0, sum2 = 0, sum3 = 0, sum4 = 0; 

    // Get sum of each category (Exam1, 2, 3, and Total)
    for(int i = 0; i < SIZE; i++)
    {
        sum1 += arr[i].exam1;
        sum2 += arr[i].exam2; 
        sum3 += arr[i].exam3;
        sum4 += arr[i].total; 
    }

    // Calculate average for each category 
    average1 += static_cast<double>(sum1)/size;  

    average2 += static_cast<double>(sum2)/size; 

    average3 += static_cast<double>(sum3)/size; 

    average4 += static_cast<double>(sum4)/size; 

    // Loop average values into an array of size 4 
    for(int index = 0; index < INFO; index++)
    {
        if(index == 0)
            average[0] = average1; 
        else if(index == 1)
            average[1] = average2; 
        else if(index == 2)
            average[2] = average3; 
        else if(index == 3)
            average[3] = average4; 
        else 
            cout << "Fail!" << endl; 
    }
}

void getStd(StudentData arr[], double &std1, double &std2, double &std3, double &std4, double &average1, double &average2, double &average3, double &average4, double standardDeviation[])
{
    double deviationSum1 = 0, deviationSum2 = 0, deviationSum3 = 0, deviationSum4 = 0; 

    for(int i = 0; i < SIZE; i++)
    {
        deviationSum1 += pow((arr[i].exam1 - average1), 2); 
        deviationSum2 += pow((arr[i].exam2 - average2), 2); 
        deviationSum3 += pow((arr[i].exam3 - average3), 2); 
        deviationSum4 += pow((arr[i].total - average4), 2);
    }

    std1 = sqrt(deviationSum1 / ((SIZE) - 1)); 
    std2 = sqrt(deviationSum2 / ((SIZE) - 1)); 
    std3 = sqrt(deviationSum3 / ((SIZE) - 1)); 
    std4 = sqrt(deviationSum4 / ((SIZE) - 1)); 

    // Loop average values into an array of size
    for(int index = 0; index < INFO; index++)
    {
        if(index == 0)
            standardDeviation[0] = std1; 
        else if(index == 1)
            standardDeviation[1] = std2; 
        else if(index == 2)
            standardDeviation[2] = std3; 
        else if(index == 3)
            standardDeviation[3] = std4; 
        else 
            cout << "Fail!" << endl; 
    }
}



    cout << "\n"; 
}

void sort(StudentData arr[])
{
    StudentData temp; 

    for (int i = 0; i < (SIZE - 1); i++)
    {
        for (int j = i + 1; j < SIZE; j++)
        {
            if (arr[i].last_name > arr[j].last_name)
            {
                temp = arr[i];    
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}
