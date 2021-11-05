// http://ovainola.github.io/jekyll/update/2016/08/07/Wrapping-C++.html

#include "class_example.h"

using namespace vehicles;

Car::Car(char* brand, char* model, int yearBought, double currentSpeed)
{
    cBrand = brand;
    cModel = model;
    mYear  = yearBought;
    mSpeed = currentSpeed;
}

Car::~Car()
{
}

double Car::getSpeed() {
    return mSpeed;
}

void Car::setSpeed(double newSpeed) {
  mSpeed = newSpeed;
}