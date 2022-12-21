import Stack from '@mui/material/Stack';
import MessageMolecule from '../../molecules/Message';

const PublishOrganism = ({ messages, sendMessageHandler }) => {
  return (
    <Stack spacing={2}>
      {messages.map((message, i) => (
        <MessageMolecule
          key={`send-message-${i}`}
          onClickHandler={() => sendMessageHandler(message.content)}
          content={message.content}
        />
      ))}
    </Stack>
  );
};

export default PublishOrganism;
