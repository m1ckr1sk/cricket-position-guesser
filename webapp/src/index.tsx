import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom/client";

const positionDescriptions: Record<string, string> = {
    "mid-on": "Correct! Mid-on is near the bowler.",
    "cover point": "Correct! Cover Point is near the off-side area.",
};

const CricketPositionGuesser: React.FC = () => {
    const [input, setInput] = useState("");
    const [result, setResult] = useState("");
    const [apiMessage, setApiMessage] = useState<string>("");
    const [gameId, setGameId] = useState<string | null>(null);

    useEffect(() => {
        // Example: fetch from /api/hello or any endpoint you want
        fetch("http://localhost:5173/game/", {
            method: "POST"
        })
            .then((res) => res.ok ? res.json() : Promise.reject("API error"))
            .then((data) => {
                setGameId(data.game_id);
                setApiMessage("Game started!");
            })
            .catch(() => setApiMessage("API unavailable"));
    }, []);

    const handleGuess = async () => {
        if (!gameId) {
            setResult("Game not initialized.");
            return;
        }
        const guess = input.trim();
        if (!guess) {
            setResult("Please enter a position.");
            return;
        }
        try {
            const response = await fetch("http://localhost:5173/guess/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ game_id: gameId, guess }),
            });
            if (!response.ok) throw new Error("API error");
            const data = await response.json();
            setResult(`Status: ${data.status}, Rating: ${data.distance_rating}`);
        } catch {
            setResult("API unavailable or error processing guess.");
        }
    };

    return (
        <div style={{ fontFamily: "Arial, sans-serif", backgroundColor: "#f3f3f3", minHeight: "100vh", margin: 0 }}>
            <header style={{ backgroundColor: "#2a6dcb", color: "white", padding: 20, textAlign: "center" }}>
                <h1>Guess Cricket Positions</h1>
            </header>
            <main style={{
                margin: "20px auto",
                maxWidth: 600,
                background: "white",
                padding: 20,
                borderRadius: 10,
                boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)"
            }}>
                <div style={{ marginBottom: 20, color: "#888" }}>
                    {apiMessage}
                </div>
                <form
                    id="cricketForm"
                    onSubmit={e => {
                        e.preventDefault();
                        handleGuess();
                    }}
                >
                    <label htmlFor="position" style={{ display: "block", marginBottom: 10, fontWeight: "bold" }}>
                        Enter the name of a cricket position:
                    </label>
                    <input
                        type="text"
                        id="position"
                        name="position"
                        placeholder="e.g., Mid-on, Cover Point"
                        value={input}
                        onChange={e => setInput(e.target.value)}
                        style={{
                            width: "100%",
                            padding: 10,
                            marginBottom: 20,
                            border: "1px solid #ccc",
                            borderRadius: 5
                        }}
                    />
                    <button
                        type="submit"
                        style={{
                            backgroundColor: "#2a6dcb",
                            color: "white",
                            border: "none",
                            padding: "10px 20px",
                            borderRadius: 5,
                            cursor: "pointer"
                        }}
                    >
                        Submit
                    </button>
                </form>
                <div className="result" style={{ marginTop: 20, fontSize: "1.2em" }}>{result}</div>
            </main>
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById("root")!);
root.render(<CricketPositionGuesser />);