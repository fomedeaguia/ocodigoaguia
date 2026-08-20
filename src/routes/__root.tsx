import { createRootRoute, Outlet, ScrollRestoration } from "@tanstack/react-router";
import { Footer } from "@/components/landing/Footer";

export const Route = createRootRoute({
  component: Root,
});

function Root() {
  return (
    <>
      <ScrollRestoration />
      <Outlet />
      <Footer />
    </>
  );
}
