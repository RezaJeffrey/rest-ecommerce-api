interface Prob {
  text: string;
}

function Button({ text }: Prob) {
  return (
    <button type="button" className="btn btn-primary">
      {text}
    </button>
  );
}

export default Button;
