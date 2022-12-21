import Grid from '@mui/material/Grid';
import { useState } from 'react';
import logo from '../../logo.png';
import PublishOrganism from '../../organisms/Publish';
import ReadOrganism from '../../organisms/Read';

const availableMessages = [
  { content: 'Workshop' },
  { content: 'Walmart' },
  { content: 'Este es el lugar' },
];

const ManageMessages = ({ messageRepository }) => {
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
            messages={availableMessages}
            sendMessageHandler={sendMessage}
          />
        </Grid>
        <Grid item xs={6}>
          <ReadOrganism
            messages={messages}
            readMessagesHandler={readMessages}
          />
        </Grid>
      </Grid>
    </Grid>
  );
};

export default ManageMessages;
