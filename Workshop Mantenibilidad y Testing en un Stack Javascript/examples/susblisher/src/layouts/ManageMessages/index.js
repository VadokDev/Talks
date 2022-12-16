import Grid from '@mui/material/Grid';
import { useState } from 'react';
import Message from '../../molecules/Message';
import logo from '../../logo.png';

const availableMessages = [
  { content: 'Workshop' },
  { content: 'Walmart' },
  { content: 'Este es el lugar' },
];

const ManageMessages = ({
  PublishOrganism,
  ReadOrganism,
  messageRepository,
}) => {
  const [messages, setMessages] = useState([]);

  const readMessages = () => {
    messageRepository
      .getMessages()
      .then((newMessages) => setMessages(newMessages));
  };

  const sendMessage = (content) => {
    messageRepository.sendMessage(content).then(() => readMessages());
  };

  return (
    <Grid container direction='column' alignItems={'center'}>
      <Grid item pb={5}>
        <img src={logo} alt='Walmart Chile'></img>
      </Grid>
      <Grid container spacing={2}>
        <Grid item xs={6}>
          <PublishOrganism
            MessageMolecule={Message}
            messages={availableMessages}
            sendMessageHandler={sendMessage}
          />
        </Grid>
        <Grid item xs={6}>
          <ReadOrganism
            MessageMolecule={Message}
            messages={messages}
            readMessagesHandler={readMessages}
          />
        </Grid>
      </Grid>
    </Grid>
  );
};

export default ManageMessages;
