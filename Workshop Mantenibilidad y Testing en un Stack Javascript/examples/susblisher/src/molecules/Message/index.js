import Button from '@mui/material/Button';

const MessageMolecule = ({ content, onClickHandler }) => {
  return (
    <Button onClick={onClickHandler} variant='outlined'>
      {content}
    </Button>
  );
};

export default MessageMolecule;
