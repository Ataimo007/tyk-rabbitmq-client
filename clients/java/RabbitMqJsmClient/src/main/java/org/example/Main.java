package org.example;

import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.ConnectionFactory;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

//import javax.jms.Connection;
//import javax.jms.ConnectionFactory;
//import javax.jms.JMSException;
//import javax.jms.MessageProducer;
//import javax.jms.Session;
//import javax.jms.TextMessage;
//import org.apache.qpid.jms.JmsConnectionFactory;

public class Main {

    private static final String userName = "ataimo@tyk.io";
    private static final String password = "alex1234.";
//    private static final String virtualHost = "";
    private static final String hostName = "localhost";
//    private static final int portNumber = 5672;
    private static final int portNumber = 8081;

    public static void main(String[] args) throws IOException, TimeoutException {
        System.out.println("Hello world!");

        String queueName = "tyk-java-client";
        String message = "Hello, RabbitMQ and Java Client Library - This if from Tyk";

        ConnectionFactory factory = new ConnectionFactory();

        // "guest"/"guest" by default, limited to localhost connections
        factory.setUsername(userName);
        factory.setPassword(password);
//        factory.setVirtualHost(virtualHost);
        factory.setHost(hostName);
        factory.setPort(portNumber);

        Connection conn = factory.newConnection();

        // Create channel
        Channel channel = conn.createChannel();

        // Declare queue
        channel.queueDeclare(queueName, false, false, false, null);

        // Publish message
        channel.basicPublish("", queueName, null, message.getBytes());
        System.out.println("Message sent successfully!");

        // Close resources
        channel.close();
        conn.close();
    }
}