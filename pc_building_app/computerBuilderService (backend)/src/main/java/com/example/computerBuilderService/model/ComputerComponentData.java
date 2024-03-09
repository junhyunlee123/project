package com.example.computerBuilderService.model;

public class ComputerComponentData {
    private int productID;
    private String productName;
    private double price;
    private String productImage;
    private String productDetailURL;

    public ComputerComponentData() {
    }

    public ComputerComponentData(int productID, String productName, double price, String productImage, String productDetailURL) {
        this.productID = productID;
        this.productName = productName;
        this.price = price;
        this.productImage = productImage;
        this.productDetailURL = productDetailURL;
    }

    public int getProductID() {
        return productID;
    }

    public void setProductID(int productID) {
        this.productID = productID;
    }


    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }


    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }


    public String getProductImage() {
        return productImage;
    }

    public void setProductImage(String productImage) {
        this.productImage = productImage;
    }


    public String getProductDetailURL() {
        return productDetailURL;
    }

    public void setProductDetailURL(String productDetailURL) {
        this.productDetailURL = productDetailURL;
    }


    @Override
    public String toString() {
        return "ComputerComponentData{" +
                "productID=" + productID +
                ", productName='" + productName + '\'' +
                ", price=" + price +
                ", productImage='" + productImage + '\'' +
                ", productDetailURL='" + productDetailURL +'\'' +
                '}';
    }
}
