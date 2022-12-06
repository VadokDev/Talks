import Stack from '@mui/material/Stack';

const Publish = ({ MessageMolecule, messages, sendMessageHandler }) => {
  return (
    <Stack spacing={2}>
      {messages.map((message) => (
        <MessageMolecule
          onClickHandler={() => sendMessageHandler(message.content)}
          content={message.content}
        />
      ))}
    </Stack>
  );
};

export default Publish;
