package fixture

// Fixture for #1514: the gosec marker is spelled `#nosec`, distinct from
// bandit's bare `nosec`, so both ids must be exercised separately.
import "os/exec"

func Run(cmd string) ([]byte, error) {
	return exec.Command("sh", "-c", cmd).Output() //#nosec G204
}
