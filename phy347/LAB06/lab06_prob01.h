#ifndef lab06_prob01_H
#define lab06_prob01_H

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

class Time {
 public:
  Time();
  void setHour( int );
  void setMinute( int );
  void setSecond( int );
  int getHour( void ) const;
  int getMinute( void ) const;
  int getSecond( void ) const;
  void printStandard( void ) const;
 private:
  int hour;
  int minute;
  int second;
};

#endif

Time::Time()
{
  long int totalTime;   // time in seconds since 1970
  int currentYear = 2017 - 1970; // current year
  double totalYear;     // current time in years
  double totalDay;      // days since beginning of year
  double day;           // current time in days
  long double divisor;  // conversion divisor
  int timeShift = 2;    // time returned by time() is
  // given as the number of seconds
  // elapsed since 1/1/70 GMT.
  
  totalTime = time( NULL );
  divisor = ( 60.0 * 60.0 * 24.0 * 365.0 );
  totalYear = totalTime / divisor - currentYear;
  totalDay = 365 * totalYear; // leap years ignored
  day = totalDay - ( int ) totalDay;
  
  setHour( day * 24 + timeShift );
  setMinute( ( day * 24 - ( int )( day * 24 ) ) * 60 );
  setSecond( ( day * 24 * 60 - ( int )( day * 24 * 60 ) ) * 60 );
}

void Time::setHour( int h ) { hour = ( h >= 0 && h < 24 ) ? h : 0; }

void Time::setMinute( int m ) { minute = ( m >= 0 && m < 60 ) ? m : 0; }

void Time::setSecond( int s ) { second = ( s >= 0 && s < 60 ) ? s : 0; }

int Time::getHour() const { return hour; }

int Time::getMinute() const { return minute; }

int Time::getSecond() const { return second; }

void Time::printStandard() const {
  cout << ( ( hour % 12 == 0 ) ? 12 : hour % 12 ) << ":"
       << ( minute < 10 ? "0" : "" ) << minute << ":"
       << ( second < 10 ? "0" : "" ) << second
       << ( hour < 12 ? " AM" : " PM" ) << endl;
}
