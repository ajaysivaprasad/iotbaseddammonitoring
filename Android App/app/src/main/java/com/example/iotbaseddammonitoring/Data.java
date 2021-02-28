package com.example.iotbaseddammonitoring;

public class Data {

    private String Humidity,Temperature,WaterLevel,VibrationLevel;

    public Data() {
    }

    public Data(String Humidity, String Temperature,String WaterLevel, String VibrationLevel) {
        this.Humidity = Humidity;
        this.Temperature = Temperature;
        this.WaterLevel = WaterLevel;
        this.VibrationLevel = VibrationLevel;
    }

    public void setHumidity(String text) {
        this.Humidity = text;
    }
    public void setTemperature(String text) {
        this.Temperature = text;
    }
    public void setWaterLevel(String text) {
        this.WaterLevel = text;
    }
    public void setVibrationLevel(String text) {
        this.VibrationLevel = text;
    }


    public String getHumidity() {
        return Humidity;
    }
    public String getTemperature() {
        return Temperature;
    }
    public String getWaterLevel() {
        return WaterLevel;
    }
    public String getVibrationLevel() {
        return VibrationLevel;
    }
}