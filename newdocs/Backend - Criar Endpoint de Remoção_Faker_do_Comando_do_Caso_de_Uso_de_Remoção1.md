```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public partial static class BrandHelper
    {
        private static Faker<DeleteBrandCommand> FakeDeleteBrandCommand(
            string? id = null,
            string? organizationId = null)
        {
            return new Faker<DeleteBrandCommand>()
                .CustomInstantiator(f => new DeleteBrandCommand(
                    id ?? f.Random.String2(10),
                    organizationId ?? f.Random.String2(10)));
        }

        public static DeleteBrandCommand RandomDeleteBrandCommand(
            string? id = null,
            string? organizationId = null)
        {
            return FakeDeleteBrandCommand(id, organizationId).Generate();
        }
    }
}
```