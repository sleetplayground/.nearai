# Authentication and Secrets Management in NEAR AI Agents

## Overview
This document explains how authentication and secrets management work in NEAR AI agents, covering both user authentication through NEAR wallets and the handling of various types of secrets and API keys.

## User Authentication

### NEAR Wallet Integration
When users interact with your NEAR AI agent, authentication happens automatically through the NEAR wallet system. Here's how it works:

1. **Automatic Authentication**: Users are automatically prompted to connect their NEAR wallet when they first interact with an agent that requires authentication.
2. **Wallet Connection**: The user approves the connection through their NEAR wallet (either NEAR Wallet, MyNearWallet, or other compatible wallets).
3. **Account Access**: Once connected, the agent can access the user's NEAR account address and perform authorized actions.

### Authentication Flow
```
User -> NEAR Wallet -> Agent
1. User initiates interaction
2. Wallet prompts for connection
3. User approves connection
4. Agent receives user's account information
```

## Secrets Management

### Types of Secrets

1. **Agent-Level Secrets**
   - These are secrets that belong to your agent itself
   - Examples: API keys for external services, database credentials
   - These secrets are used by the agent regardless of which user is interacting
   - Must be configured by the agent developer

2. **User-Specific Secrets**
   - These belong to individual users
   - Examples: NEAR wallet credentials, personal API keys
   - Each user maintains their own secrets
   - Automatically handled by the NEAR wallet system

### How Secrets Work

#### Agent-Level Secrets
- You (the developer) must configure these in your agent's settings
- Users will use your agent's secrets when interacting with external services
- Example: If your agent uses OpenAI's API, it will use your API key

#### User-Specific Secrets
- Users use their own NEAR wallet credentials automatically
- When your agent needs to perform transactions:
  1. The transaction is initiated by your agent
  2. User's wallet prompts for approval
  3. Transaction is signed with user's credentials

### Best Practices

1. **Never Expose Agent Secrets**
   - Don't include secrets in your code
   - Use environment variables or secure secret management
   - Never log or display secret values

2. **Minimal Privilege**
   - Only request necessary wallet permissions
   - Use temporary access when possible

3. **Clear Communication**
   - Inform users what permissions you're requesting
   - Explain why certain wallet access is needed

## Examples

### Basic Wallet Integration
```javascript
// The wallet connection is handled automatically
// You don't need to write specific code for it

// Example of a contract call using user's credentials
async function makeContractCall() {
  // The contract call will automatically trigger the user's wallet
  // for approval and use their credentials for signing
  const result = await contract.someMethod({
    args: { /* method arguments */ },
  });
}
```

### Using Agent-Level Secrets
```javascript
// Your agent's secrets are securely stored and accessed
// Users don't need to provide these secrets
const apiCall = async () => {
  // Your agent's API key is used here
  const response = await fetch('https://api.example.com', {
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY'
    }
  });
};
```

## Summary
- User authentication is handled automatically through NEAR wallet
- Agent-level secrets (your API keys) are used for external services
- User-specific secrets (wallet credentials) are handled by the NEAR wallet system
- No additional setup is required for basic wallet integration
- You only need to configure agent-level secrets if your agent uses external services

## Security Considerations
1. Always use secure methods to store agent-level secrets
2. Never request more wallet permissions than necessary
3. Be transparent about how you use user's wallet access
4. Implement proper error handling for failed authentications
5. Regular audit of your agent's security practices

For more information about NEAR smart contract integration, refer to [near_smart_contract_integration.md](near_smart_contract_integration.md).