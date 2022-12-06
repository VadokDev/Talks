import Grid from '@mui/material/Grid';
import { useState } from 'react';
import Message from '../../molecules/Message';

const availableMessages = [
  { content: 'ola' },
  { content: 'qué' },
  { content: 'talca' },
];

const ManageMessages = ({
  PublishOrganism,
  ReadOrganism,
  messageRepository,
}) => {
  const [messages, setMessages] = useState([]);

  const readMessages = () => {
    messageRepository.getMessages().then((messages) => setMessages(messages));
  };

  const sendMessage = (content) => {
    messageRepository.sendMessage(content).then(() => readMessages(messages));
  };

  return (
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
  );
};

export default ManageMessages;
