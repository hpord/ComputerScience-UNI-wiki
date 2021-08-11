import React, { useRef, useState, useEffect } from "react";
import { Paper, TextField, Button, makeStyles } from "@material-ui/core";
import Particles from 'react-particles-js';

import useChat from "./useChatRoom";
import clsx from "clsx";

const useStyles = makeStyles({
  container: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: "100vh",
    backgroundColor: '#000000'
  },
  paper: {
    width: "50em",
    height: "80%",
    position: "relative"
  },
  action: {
    display: "flex",
    width: "96%",
    alignItems: "center",
    margin: "1em",
    position: "absolute",
    bottom: 0
  },
  sendButton: {
    width: "10em",
    height: "50%",
    margin: "0 2em"
  },
  messageInput: {
    width: "100%"
  },
  messageContainer: {
    overflowY: "auto",
    height: "85%"
  },
  divider: {
    margin: "0.1em"
  },
  message: {
    listStyle: "none"
  },
  owner: {
    margin: "1em",
    backgroundColor: "#0091EA",
    padding: "0.5em 1.5em",
    borderRadius: "20px",
    color: "#FFF",
    wordBreak: "break-word",
    maxWidth: "65%",
    width: "fit-content",
    marginRight: "auto"
  },
  guest: {
    margin: "1em",
    backgroundColor: "#8BC34A",
    padding: "0.5em 1.5em",
    borderRadius: "20px",
    color: "#FFF",
    wordBreak: "break-word",
    maxWidth: "65%",
    width: "fit-content",
    marginLeft: "auto"
  },
  ol: {
    paddingInlineEnd: "40px"
  }
});

const Room = () => {
  const { messages, sendMessage } = useChat();
  const [newMessage, setNewMessage] = useState("");
  const classes = useStyles();
  const messageRef = useRef()

  const handleNewMessageChange = event => {
    setNewMessage(event.target.value);
  };

  const handleSendMessage = () => {
    if (newMessage !== "") {
      sendMessage(newMessage);
      setNewMessage("");
    }
  };

  const handleKeyUp = event => {
    if (event.key === "Enter") {
      if (newMessage !== "") {
        sendMessage(newMessage);
        setNewMessage("");
      }
    }
  }

  useEffect(() => messageRef.current.scrollIntoView({ behavior: "smooth" }))

  return (
    <div className={classes.container}>
      <Particles
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          backgroundColor: '#000000'
        }}
        params={{
          "particles": {
            "number": {
              "value": 80,
              "density": {
                "enable": true,
                "value_area": 800
              }
            },
            "color": {
              "value": "#ffffff"
            },
            "opacity": {
              "value": 0.5,
              "random": false,
              "anim": {
                "enable": false,
                "speed": 1,
                "opacity_min": 0.1,
                "sync": false
              }
            },
            "size": {
              "value": 2,
              "random": true,
              "anim": {
                "enable": false,
                "speed": 40,
                "size_min": 0.1,
                "sync": false
              }
            },
            "line_linked": {
              "enable": true,
              "distance": 150,
              "color": '#ffffff',
              "opacity": 0.4,
              "width": 1
            },
            "move": {
              "enable": true,
              "speed": 1,
              "direction": 'none',
              "random": false,
              "straight": false,
              "out_mode": 'out',
              "bounce": false,
              "attract": {
                "enable": false,
                "rotateX": 600,
                "rotateY": 1200
              }
            },
          },
          "interactivity": {
            "detect_on": 'canvas',
            "events": {
              "onhover": {
                "enable": true,
                "mode": 'grab'
              },
              "onclick": {
                "enable": true,
                "mode": 'push'
              },
              "resize": true
            },
            "modes": {
              "grab":{
                "distance": 150,
                "line_linked":{
                  "opacity": 1,
                  "color": '#3555A9'
                }
              },
              "bubble": {
                "distance": 400,
                "size": 40,
                "duration": 2,
                "opacity": 8,
                "speed": 3
              },
              "repulse":{
                "distance": 200,
                "duration": 0.4
              },
              "push":{
                "particles_nb": 4,
                "color": '#3555A9'
              },
              "remove":{
                "particles_nb": 2
              }
            },
          },
          "retina_detect": true
        }}
      />
      <Paper elevation={5} className={classes.paper}>
        <div className={classes.messageContainer}>
          <ol className={classes.ol}>
            {messages.map((message, i) => (
              <li
                key={i}
                className={clsx(classes.message, message.isOwner ? classes.owner : classes.guest)}
              >
                <span>{message.body}</span>
              </li>
            ))}
          </ol>
          <div ref={messageRef}></div>
        </div>
        <div className={classes.action}>
          <TextField
            className={classes.messageInput}
            id="message"
            label="Mensaje"
            placeholder="Ingresa tu mensaje aquí"
            variant="outlined"
            value={newMessage}
            onChange={handleNewMessageChange}
            onKeyUp={handleKeyUp}
          />
          <Button
            disabled={!newMessage}
            variant="contained"
            color="primary"
            onClick={handleSendMessage}
            className={classes.sendButton}
          >
            Enviar
          </Button>
        </div>
      </Paper>

    </div>
  );
};

export default Room;